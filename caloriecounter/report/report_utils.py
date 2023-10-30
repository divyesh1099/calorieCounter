from django.db.models import Sum
from datetime import datetime
from home.models import *
from tracker.models import *
def get_monthly_report(user):
    current_year = datetime.now().year
    monthly_data = DailyIntake.objects.filter(user=user, date__year=current_year).annotate(month=models.functions.ExtractMonth('date')).values('month').annotate(
        total_calories=Sum('total_calories'),
        total_protein=Sum('total_protein'),
        total_carbs=Sum('total_carbs'),
        total_fats=Sum('total_fats')
    ).order_by('month')
    return monthly_data

def get_goal_achievement_report(user):
    daily_logs = UserDailyLog.objects.filter(user=user)
    user_profile = UserProfile.objects.get(user=user)
    
    report = []
    for log in daily_logs:
        report.append({
            'date': log.date,
            'calories_consumed': log.total_calories,
            'calories_goal': user_profile.daily_calorie_goal,
            'protein_goal': user_profile.daily_protein_goal,
            'carbs_goal': user_profile.daily_carb_goal,
            'fats_goal': user_profile.daily_fat_goal
        })
    return report

def get_comparison_report(user, start_date, end_date):
    daily_logs = UserDailyLog.objects.filter(user=user, date__range=[start_date, end_date])
    
    report = []
    for log in daily_logs:
        report.append({
            'date': log.date,
            'calories': log.total_calories,
            'protein': log.total_protein,
            'carbs': log.total_carbs,
            'fats': log.total_fat
        })
    return report
