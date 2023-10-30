from django.db import models
from django.contrib.auth.models import User

class MonthlyReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.PositiveIntegerField()  # 1 to 12
    year = models.PositiveIntegerField()
    
    average_calories = models.FloatField()
    highest_calories_day = models.DateField()
    lowest_calories_day = models.DateField()
    average_proteins = models.FloatField()
    average_carbs = models.FloatField()
    average_fats = models.FloatField()
    
    class Meta:
        unique_together = ('user', 'month', 'year')
    
    def __str__(self):
        return f"{self.user.username}'s Report for {self.month}/{self.year}"

class GoalAchievementReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.PositiveIntegerField()  # 1 to 12
    year = models.PositiveIntegerField()
    
    goal_type = models.CharField(max_length=50, choices=[
        ('CALORIE', 'Calorie Intake'),
        ('PROTEIN', 'Protein Intake'),
        ('CARB', 'Carb Intake'),
        ('FAT', 'Fat Intake'),
    ])
    goal_value = models.FloatField()
    achieved_value = models.FloatField()
    
    class Meta:
        unique_together = ('user', 'month', 'year', 'goal_type')
    
    def __str__(self):
        return f"{self.user.username}'s Goal Report for {self.month}/{self.year}"

class ComparisonReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    start_month = models.PositiveIntegerField()  # 1 to 12
    start_year = models.PositiveIntegerField()
    end_month = models.PositiveIntegerField()  # 1 to 12
    end_year = models.PositiveIntegerField()
    
    change_in_calories = models.FloatField()
    change_in_proteins = models.FloatField()
    change_in_carbs = models.FloatField()
    change_in_fats = models.FloatField()
    
    class Meta:
        unique_together = ('user', 'start_month', 'start_year', 'end_month', 'end_year')
    
    def __str__(self):
        return
