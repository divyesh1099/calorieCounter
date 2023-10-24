from django import forms
from .models import FoodLog

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog
        fields = ['food_item', 'quantity', 'meal_type']
