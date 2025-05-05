const drinksData = [
  { name: "Cappuccino", calories: 130, category: "Coffee", ingredients: "Espresso, Steamed Milk, Milk Foam", price: 4.5 },
  { name: "Mocha", calories: 290, category: "Coffee", ingredients: "Espresso, Chocolate, Steamed Milk, Whipped Cream", price: 5.0 },
  { name: "Mojito", calories: 240, category: "Cocktail", ingredients: "White Rum, Mint, Lime, Soda Water, Sugar", price: 6.0 },
  { name: "Bloody Mary", calories: 200, category: "Cocktail", ingredients: "Vodka, Tomato Juice, Lemon, Spices", price: 7.0 },
  { name: "Virgin Mojito", calories: 120, category: "Mocktail", ingredients: "Mint, Lime, Soda Water, Sugar", price: 4.0 },
  { name: "Fruit Punch", calories: 150, category: "Mocktail", ingredients: "Mixed Fruit Juices, Grenadine, Soda", price: 5.5 },
  { name: "Caramel Latte", calories: 250, category: "Coffee", ingredients: "Espresso, Steamed Milk, Caramel Syrup", price: 5.0 },
  { name: "Iced Americano", calories: 15, category: "Coffee", ingredients: "Espresso, Cold Water, Ice", price: 3.0 },
  { name: "Negroni", calories: 67, category: "Cocktail", ingredients: "Vermouth, Campari, Gin", price: 8.0 }
];

const searchInput = document.getElementById("searchInput");
const resultArea = document.getElementById("resultArea");

searchInput.addEventListener("input", () => {
  const query = searchInput.value.trim().toLowerCase();
  resultArea.innerHTML = "";

  if (query === "") {
      resultArea.innerHTML = `<p class="hint">Type a drink name to see its details.</p>`;
      return;
  }

  const match = drinksData.find(drink => drink.name.toLowerCase() === query);

  if (match) {
      resultArea.innerHTML = `
          <div class="drink-details">
              <h2>${match.name}</h2>
              <p><strong>Category:</strong> ${match.category}</p>
              <p><strong>Calories:</strong> ${match.calories}</p>
              <p><strong>Ingredients:</strong> ${match.ingredients}</p>
          </div>
      `;
  } else {
      resultArea.innerHTML = `<p class="hint">No matching drink found.</p>`;
  }
});
