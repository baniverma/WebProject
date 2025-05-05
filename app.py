from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    visit_date = db.Column(db.String(20), nullable=False)

# Routes
@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
        db.session.add(new_recipe)
        db.session.commit()
        flash("Recipe added successfully!", "success")
        return redirect(url_for('index'))
    return render_template('recipe.html', page="add")

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if request.method == 'POST':
        recipe.name = request.form['name']
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']
        db.session.commit()
        flash("Recipe updated successfully!", "success")
        return redirect(url_for('home'))
    return render_template('recipe.html', page="update", recipe=recipe)

@app.route('/delete/<int:id>')
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted successfully!", "success")
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('User already exists', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['username'] = username
            session.permanent = True  # Keep session persistent
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html')  # Fixed template rendering

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Please log in first', 'warning')
        return redirect(url_for('login'))
    return f'Hello, {session["username"]}! Welcome to your dashboard.'

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        new_review = Review(
            name=request.form['name'],
            email=request.form['email'],
            title=request.form['title'],
            message=request.form['message'],
            rating=int(request.form['rating']),
            visit_date=request.form['visit_date']
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Review submitted successfully', 'success')
    reviews = Review.query.all()
    return render_template('review.html', reviews=reviews)

# REST API User Management
class UserList(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'username': user.username} for user in users]

    def post(self):
        if not request.is_json:
            return {'error': 'Request must be JSON'}, 400
        data = request.get_json()
        if 'username' not in data or 'password' not in data:
            return {'error': 'Missing username or password'}, 400
        if User.query.filter_by(username=data['username']).first():
            return {'error': 'User already exists'}, 400
        new_user = User(username=data['username'], password_hash=generate_password_hash(data['password']))
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'username': new_user.username}, 201

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {'id': user.id, 'username': user.username}
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted'}, 200

api.add_resource(UserList, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')

if __name__ == '__main__':  
    with app.app_context():
        db.create_all()
    app.run(debug=True)