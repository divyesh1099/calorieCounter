from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import FoodLog, DailyIntake
from home.models import UserProfile, UserStatistics, UserDailyLog

@receiver(post_save, sender=FoodLog)
def update_daily_intake_and_profile(sender, instance, created, **kwargs):
    # Update or create DailyIntake for the specific date
    daily_intake, _ = DailyIntake.objects.get_or_create(
        user=instance.user,
        date=instance.date_time_consumed.date()
    )

    # Check if this is a new FoodLog or an updated one
    if created:
        # Update nutritional values for DailyIntake
        daily_intake.total_calories += instance.total_calories
        daily_intake.total_protein += instance.total_protein
        daily_intake.total_carbs += instance.total_carbs
        daily_intake.total_fats += instance.total_fats
        daily_intake.total_dietary_fiber += instance.total_dietary_fiber
        daily_intake.total_sugars += instance.total_sugars
        daily_intake.total_starch += instance.total_starch
        daily_intake.total_saturated_fats += instance.total_saturated_fats
        daily_intake.total_trans_fats += instance.total_trans_fats
        daily_intake.total_monounsaturated_fats += instance.total_monounsaturated_fats
        daily_intake.total_polyunsaturated_fats += instance.total_polyunsaturated_fats
        daily_intake.total_cholesterol += instance.total_cholesterol
        daily_intake.total_sodium += instance.total_sodium
        daily_intake.total_potassium += instance.total_potassium
        daily_intake.total_vitamin_c += instance.total_vitamin_c
        daily_intake.total_iron += instance.total_iron
        daily_intake.save()

        # Update the UserProfile's total_calories_consumed
        profile = UserProfile.objects.get(user=instance.user)
        profile.total_calories_consumed += instance.total_calories
        profile.save()

        # Update UserDailyLog (creating if needed)
        user_daily_log, _ = UserDailyLog.objects.get_or_create(
            user=instance.user,
            date=instance.date_time_consumed.date()
        )
        user_daily_log.total_calories += instance.total_calories
        user_daily_log.total_protein += instance.total_protein
        user_daily_log.total_carbs += instance.total_carbs
        user_daily_log.total_fat += instance.total_fats
        user_daily_log.save()

        # Update UserStatistics
        user_stats, _ = UserStatistics.objects.get_or_create(user=instance.user)
        user_stats.total_days_tracked += 1
        user_stats.average_daily_calories = (
            profile.total_calories_consumed / user_stats.total_days_tracked
        )

        # Calculate the new averages based on the new daily intake
        user_stats.average_daily_protein = (user_stats.average_daily_protein * (user_stats.total_days_tracked - 1) + daily_intake.total_protein) / user_stats.total_days_tracked
        user_stats.average_daily_carbs = (user_stats.average_daily_carbs * (user_stats.total_days_tracked - 1) + daily_intake.total_carbs) / user_stats.total_days_tracked
        user_stats.average_daily_fat = (user_stats.average_daily_fat * (user_stats.total_days_tracked - 1) + daily_intake.total_fats) / user_stats.total_days_tracked

        # Update highest and lowest calories if needed
        if user_daily_log.total_calories > user_stats.highest_calories_in_a_day:
            user_stats.highest_calories_in_a_day = user_daily_log.total_calories
        if user_daily_log.total_calories < user_stats.lowest_calories_in_a_day or user_stats.lowest_calories_in_a_day == 0:
            user_stats.lowest_calories_in_a_day = user_daily_log.total_calories

        user_stats.save()


@receiver(post_delete, sender=FoodLog)
def remove_from_daily_intake_and_profile(sender, instance, **kwargs):
    # Fetch the DailyIntake for the specific date
    daily_intake = DailyIntake.objects.get(
        user=instance.user,
        date=instance.date_time_consumed.date()
    )

    # Subtract nutritional values from DailyIntake
    daily_intake.total_calories -= instance.total_calories
    daily_intake.total_protein -= instance.total_protein
    daily_intake.total_carbs -= instance.total_carbs
    daily_intake.total_fats -= instance.total_fats
    daily_intake.total_dietary_fiber -= instance.total_dietary_fiber
    daily_intake.total_sugars -= instance.total_sugars
    daily_intake.total_starch -= instance.total_starch
    daily_intake.total_saturated_fats -= instance.total_saturated_fats
    daily_intake.total_trans_fats -= instance.total_trans_fats
    daily_intake.total_monounsaturated_fats -= instance.total_monounsaturated_fats
    daily_intake.total_polyunsaturated_fats -= instance.total_polyunsaturated_fats
    daily_intake.total_cholesterol -= instance.total_cholesterol
    daily_intake.total_sodium -= instance.total_sodium
    daily_intake.total_potassium -= instance.total_potassium
    daily_intake.total_vitamin_c -= instance.total_vitamin_c
    daily_intake.total_iron -= instance.total_iron
    daily_intake.save()

    # Update the UserProfile's total_calories_consumed
    profile = UserProfile.objects.get(user=instance.user)
    profile.total_calories_consumed -= instance.total_calories
    profile.save()

    # Update UserDailyLog
    user_daily_log = UserDailyLog.objects.get(
        user=instance.user,
        date=instance.date_time_consumed.date()
    )
    user_daily_log.total_calories -= instance.total_calories
    user_daily_log.total_protein -= instance.total_protein
    user_daily_log.total_carbs -= instance.total_carbs
    user_daily_log.total_fat -= instance.total_fats
    user_daily_log.save()

    # Update UserStatistics
    user_stats = UserStatistics.objects.get(user=instance.user)
    user_stats.total_days_tracked -= 1

    if user_stats.total_days_tracked == 0:
        # If no days are tracked anymore, set all average values to zero
        user_stats.average_daily_calories = 0
        user_stats.average_daily_protein = 0
        user_stats.average_daily_carbs = 0
        user_stats.average_daily_fat = 0
    else:
        # Calculate the new averages based on the updated daily intake
        user_stats.average_daily_calories = (
            profile.total_calories_consumed / user_stats.total_days_tracked
        )
        user_stats.average_daily_protein = (
            (user_stats.average_daily_protein * (user_stats.total_days_tracked + 1) - daily_intake.total_protein) / user_stats.total_days_tracked
        )
        user_stats.average_daily_carbs = (
            (user_stats.average_daily_carbs * (user_stats.total_days_tracked + 1) - daily_intake.total_carbs) / user_stats.total_days_tracked
        )
        user_stats.average_daily_fat = (
            (user_stats.average_daily_fat * (user_stats.total_days_tracked + 1) - daily_intake.total_fats) / user_stats.total_days_tracked
        )

    user_stats.save()
