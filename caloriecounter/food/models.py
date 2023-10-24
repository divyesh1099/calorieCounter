from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Food Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    serving_size = models.FloatField(help_text="Serving size in grams")
    
    # Basic Macronutrients
    calories = models.FloatField(help_text="Calories per serving (kcal)")
    protein = models.FloatField(help_text="Protein content per serving (g)")
    total_carbohydrates = models.FloatField(help_text="Total Carbohydrates content per serving (g)")
    total_fats = models.FloatField(help_text="Total Fats content per serving (g)")
    
    # Detailed Carbohydrates
    dietary_fiber = models.FloatField(blank=True, null=True, help_text="Dietary fiber content per serving (g)")
    sugars = models.FloatField(blank=True, null=True, help_text="Sugars content per serving (g)")
    starch = models.FloatField(blank=True, null=True, help_text="Starch content per serving (g)")
    
    # Detailed Fats
    saturated_fats = models.FloatField(blank=True, null=True, help_text="Saturated Fats content per serving (g)")
    trans_fats = models.FloatField(blank=True, null=True, help_text="Trans Fats content per serving (g)")
    monounsaturated_fats = models.FloatField(blank=True, null=True, help_text="Monounsaturated Fats content per serving (g)")
    polyunsaturated_fats = models.FloatField(blank=True, null=True, help_text="Polyunsaturated Fats content per serving (g)")
    cholesterol = models.FloatField(blank=True, null=True, help_text="Cholesterol content per serving (mg)")
    
    # Micronutrients (as before)
    sodium = models.FloatField(blank=True, null=True, help_text="Sodium content per serving (mg)")
    potassium = models.FloatField(blank=True, null=True, help_text="Potassium content per serving (mg)")
    vitamin_c = models.FloatField(blank=True, null=True, help_text="Vitamin C content per serving (mg)")
    iron = models.FloatField(blank=True, null=True, help_text="Iron content per serving (mg)")

    # Additional fields
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    image = models.ImageField(upload_to='food_items/', blank=True, null=True, verbose_name="Food Image")

    class Meta:
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"
        ordering = ["name"]

    def __str__(self):
        return self.name
