# from django.db.models import Avg, Max, Min, Q, F, Sum
# from django.db.models.functions import Coalesce
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from tracker.models import FoodLog
# from report.models import MonthlyReport, GoalAchievementReport, ComparisonReport
# from django.db.models import FloatField

# @receiver(post_save, sender=FoodLog)
# def _generate_or_update_monthly_report(sender, instance, **kwargs):
#     user = instance.user
#     month = instance.date_time_consumed.month
#     year = instance.date_time_consumed.year

#     logs_for_month = FoodLog.objects.filter(
#         user=user,
#         date_time_consumed__month=month,
#         date_time_consumed__year=year
#     ).annotate(
#         calculated_calories=F('food_item__calories') * F('quantity'),
#         calculated_proteins=F('food_item__protein') * F('quantity'),
#         calculated_carbs=F('food_item__total_carbohydrates') * F('quantity'),
#         calculated_fats=F('food_item__total_fats') * F('quantity')
#     )

#     aggregated_data = logs_for_month.aggregate(
#         total_calories=Coalesce(Sum(F('food_item__calories') * F('quantity'), output_field=FloatField()), 0),
#         avg_calories=Coalesce(Avg(F('food_item__calories') * F('quantity'), output_field=FloatField()), 0),
#         max_calories=Coalesce(Max(F('food_item__calories') * F('quantity'), output_field=FloatField()), 0),
#         min_calories=Coalesce(Min(F('food_item__calories') * F('quantity'), output_field=FloatField()), 0),
#         avg_proteins=Coalesce(Avg(F('food_item__protein') * F('quantity'), output_field=FloatField()), 0),
#         avg_carbs=Coalesce(Avg(F('food_item__total_carbohydrates') * F('quantity'), output_field=FloatField()), 0),
#         avg_fats=Coalesce(Avg(F('food_item__total_fats') * F('quantity'), output_field=FloatField()), 0),
#     )

#     monthly_report, created = MonthlyReport.objects.update_or_create(
#     user=user, month=month, year=year,
#     defaults={
#         'average_calories': aggregated_data['avg_calories'] or 0,
#         'highest_calories_day': aggregated_data['max_calories'] or 0,  # this might be problematic if it's supposed to store a date
#         'lowest_calories_day': aggregated_data['min_calories'] or 0,  # same here
#         'average_proteins': aggregated_data['avg_proteins'] or 0,
#         'average_carbs': aggregated_data['avg_carbs'] or 0,
#         'average_fats': aggregated_data['avg_fats'] or 0,
#         }
#     )

#     monthly_report.average_calories = aggregated_data['avg_calories']
#     monthly_report.average_proteins = aggregated_data['avg_proteins']
#     monthly_report.average_carbs = aggregated_data['avg_carbs']
#     monthly_report.average_fats = aggregated_data['avg_fats']
#     monthly_report.highest_calories_day = aggregated_data['max_calories_day']
#     monthly_report.lowest_calories_day = aggregated_data['min_calories_day']

#     monthly_report.save()

# @receiver(post_save, sender=FoodLog)
# def update_goal_achievement_report(sender, instance, **kwargs):
#     user = instance.user
#     month = instance.date_time_consumed.month
#     year = instance.date_time_consumed.year
    
#     # Assuming you have a predefined goal for each nutrient somewhere
#     calorie_goal = 2000  # Replace with actual goal, can be fetched from a model or config
#     protein_goal = 100  # Same here
#     carb_goal = 200  # And here
#     fat_goal = 50  # And here

#     logs_this_month = FoodLog.objects.filter(user=user, date_time_consumed__month=month, date_time_consumed__year=year)
#     total_calories_this_month = sum([log.total_calories for log in logs_this_month])
#     total_protein_this_month = sum([log.total_protein for log in logs_this_month])
#     total_carbs_this_month = sum([log.total_carbs for log in logs_this_month])
#     total_fats_this_month = sum([log.total_fats for log in logs_this_month])

#     # Create or Update GoalAchievementReport
#     report_calorie, created = GoalAchievementReport.objects.get_or_create(user=user, month=month, year=year, goal_type='CALORIE')
#     report_calorie.goal_value = calorie_goal
#     report_calorie.achieved_value = total_calories_this_month
#     report_calorie.save()

#     report_protein, created = GoalAchievementReport.objects.get_or_create(user=user, month=month, year=year, goal_type='PROTEIN')
#     report_protein.goal_value = protein_goal
#     report_protein.achieved_value = total_protein_this_month
#     report_protein.save()

#     # Similarly, do this for carbs and fats

# @receiver(post_save, sender=FoodLog)
# def update_comparison_report(sender, instance, **kwargs):
#     user = instance.user
#     month = instance.date_time_consumed.month
#     year = instance.date_time_consumed.year

#     # Assuming you want to compare to the previous month
#     if month == 1:
#         prev_month = 12
#         prev_year = year - 1
#     else:
#         prev_month = month - 1
#         prev_year = year

#     current_report = MonthlyReport.objects.filter(user=user, month=month, year=year).first()
#     prev_report = MonthlyReport.objects.filter(user=user, month=prev_month, year=prev_year).first()

#     if not current_report or not prev_report:
#         return

#     change_in_calories = current_report.average_calories - prev_report.average_calories
#     change_in_proteins = current_report.average_proteins - prev_report.average_proteins
#     change_in_carbs = current_report.average_carbs - prev_report.average_carbs
#     change_in_fats = current_report.average_fats - prev_report.average_fats

#     comparison, created = ComparisonReport.objects.get_or_create(
#         user=user, 
#         start_month=prev_month, start_year=prev_year, 
#         end_month=month, end_year=year
#     )
#     comparison.change_in_calories = change_in_calories
#     comparison.change_in_proteins = change_in_proteins
#     comparison.change_in_carbs = change_in_carbs
#     comparison.change_in_fats = change_in_fats
#     comparison.save()
