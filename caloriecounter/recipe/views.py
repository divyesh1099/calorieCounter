from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    """
    Render the index page displaying a list of all recipes.
    """
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe/index.html', context)

def recipe_detail(request, recipe_id):
    """
    Render the details of a single recipe.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe/recipe_detail.html', context)