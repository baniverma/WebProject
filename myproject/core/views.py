from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def index2(request):
    return render(request, 'core/index2.html')

def nutrition(request):
    return render(request, 'core/nutrition.html')

def recipe(request):
    return render(request, 'core/recipe.html')

def register(request):
    return render(request, 'core/register.html')

def review(request):
    return render(request, 'core/review.html')


def calories(request):
    return render(request, 'core/calories.html')
