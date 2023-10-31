from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories_per_100g = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    preparation_time = models.DurationField()  # in minutes
    serves = models.PositiveIntegerField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)

    def __str__(self):
        return self.name

    def total_calories(self):
        return sum(ri.calories() for ri in self.recipeingredient_set.all())

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_in_grams = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity_in_grams}g"

    def calories(self):
        return (self.ingredient.calories_per_100g * self.quantity_in_grams) / 100

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.recipe.name}"