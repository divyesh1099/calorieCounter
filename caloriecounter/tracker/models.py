from django.db import models
from django.contrib.auth.models import User
from food.models import FoodItem
from django.utils import timezone

# Create your models here.

class MealType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    meal_type = models.ForeignKey(MealType, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField(help_text="Quantity in servings or pieces")
    date_time_consumed = models.DateTimeField()

    @property
    def total_calories(self):
        return self.food_item.calories * self.quantity

    @property
    def total_protein(self):
        return self.food_item.protein * self.quantity
    
    @property
    def total_carbs(self):
        return self.food_item.total_carbohydrates * self.quantity

    @property
    def total_fats(self):
        return self.food_item.total_fats * self.quantity

    @property
    def total_dietary_fiber(self):
        return self.food_item.dietary_fiber * self.quantity

    @property
    def total_sugars(self):
        return self.food_item.sugars * self.quantity

    @property
    def total_starch(self):
        return self.food_item.starch * self.quantity

    @property
    def total_saturated_fats(self):
        return self.food_item.saturated_fats * self.quantity

    @property
    def total_trans_fats(self):
        return self.food_item.trans_fats * self.quantity

    @property
    def total_monounsaturated_fats(self):
        return self.food_item.monounsaturated_fats * self.quantity

    @property
    def total_polyunsaturated_fats(self):
        return self.food_item.polyunsaturated_fats * self.quantity

    @property
    def total_cholesterol(self):
        return self.food_item.cholesterol * self.quantity

    @property
    def total_sodium(self):
        return self.food_item.sodium * self.quantity

    @property
    def total_potassium(self):
        return self.food_item.potassium * self.quantity

    @property
    def total_vitamin_c(self):
        return self.food_item.vitamin_c * self.quantity

    @property
    def total_iron(self):
        return self.food_item.iron * self.quantity
    
    def save(self, *args, **kwargs):
        if not self.id:  # or "if not self.pk" - this checks if the object is being created and not updated
            self.date_time_consumed = timezone.localtime(timezone.now())
        super(FoodLog, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.food_item.name} by {self.user.username} on {self.date_time_consumed}"

class DailyIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    total_calories = models.FloatField(default=0)
    total_protein = models.FloatField(default=0)
    total_carbs = models.FloatField(default=0)
    total_fats = models.FloatField(default=0)
    total_dietary_fiber = models.FloatField(default=0)
    total_sugars = models.FloatField(default=0)
    total_starch = models.FloatField(default=0)
    total_saturated_fats = models.FloatField(default=0)
    total_trans_fats = models.FloatField(default=0)
    total_monounsaturated_fats = models.FloatField(default=0)
    total_polyunsaturated_fats = models.FloatField(default=0)
    total_cholesterol = models.FloatField(default=0)
    total_sodium = models.FloatField(default=0)
    total_potassium = models.FloatField(default=0)
    total_vitamin_c = models.FloatField(default=0)
    total_iron = models.FloatField(default=0)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"Intake for {self.user.username} on {self.date}"