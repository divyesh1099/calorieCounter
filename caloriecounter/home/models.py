from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(blank=True)
    target_daily_calories = models.PositiveIntegerField(default=2400)  # User's target calorie intake per day
    total_calories_consumed = models.PositiveIntegerField(default=0)  # Total Calories Consumed Today
    total_proteins_consumed = models.PositiveIntegerField(default=0)
    total_carbs_consumed = models.PositiveIntegerField(default=0)
    total_fats_consumed = models.PositiveIntegerField(default=0)
    joined_date = models.DateField(auto_now_add=True)

    # Macronutrient targets
    target_protein = models.FloatField(default=360)  # in grams
    target_carbs = models.FloatField(default=75)  # in grams
    target_fat = models.FloatField(default=66)  # in grams

    def __str__(self):
        return self.user.username

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    DIETARY_CHOICES = [
        ('VEG', 'Vegetarian'),
        ('NON_VEG', 'Non-Vegetarian'),
        ('VEGAN', 'Vegan'),
    ]
    dietary_preference = models.CharField(max_length=100, choices=DIETARY_CHOICES, default='VEG')
    send_email_notifications = models.BooleanField(default=True)

    THEME_CHOICES = [
        ('LIGHT', 'Light Mode'),
        ('DARK', 'Dark Mode'),
    ]
    theme_preference = models.CharField(max_length=50, choices=THEME_CHOICES, default='LIGHT')

    def __str__(self):
        return f"{self.user.username}'s Settings"

class UserStatistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    highest_calories_in_a_day = models.PositiveIntegerField(default=0)
    lowest_calories_in_a_day = models.PositiveIntegerField(default=0)
    average_daily_calories = models.FloatField(default=0)
    total_days_tracked = models.PositiveIntegerField(default=0)

    # Macronutrient statistics
    average_daily_protein = models.FloatField(default=0)  # in grams
    average_daily_carbs = models.FloatField(default=0)  # in grams
    average_daily_fat = models.FloatField(default=0)  # in grams

    def __str__(self):
        return f"{self.user.username}'s Statistics"

class UserDailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_calories = models.PositiveIntegerField(default=0)  # Calories consumed in this day

    # Macronutrients consumed for the day
    total_protein = models.FloatField(default=0)  # in grams
    total_carbs = models.FloatField(default=0)  # in grams
    total_fat = models.FloatField(default=0)  # in grams

    def calorie_deficit(self):
        # Assuming the UserProfile has been set up for the user
        target = UserProfile.objects.get(user=self.user).target_daily_calories
        return target - self.total_calories

    def __str__(self):
        return f"{self.user.username}'s Log for {self.date}"
