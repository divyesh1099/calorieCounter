from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'report/index.html')

@login_required
def monthly_reports(request):
    monthly_reports = MonthlyReport.objects.filter(user=request.user)
    context = {'monthly_reports': monthly_reports}
    return render(request, 'report/monthly_reports.html', context)

@login_required
def goal_achievement_reports(request):
    goal_reports = GoalAchievementReport.objects.filter(user=request.user)
    context = {'goal_reports': goal_reports}
    return render(request, 'report/goal_achievement_reports.html', context)

@login_required
def comparison_reports(request):
    comparison_reports = ComparisonReport.objects.filter(user=request.user)
    context = {'comparison_reports': comparison_reports}
    return render(request, 'report/comparison_reports.html', context)