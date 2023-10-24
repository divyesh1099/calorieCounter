from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MealType)
admin.site.register(FoodLog)
admin.site.register(DailyIntake)