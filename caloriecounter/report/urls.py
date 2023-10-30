from django.urls import path
from . import views
app_name='report'
urlpatterns=[
    path('', views.index, name='index'),
    path('monthly_reports', views.monthly_reports, name='monthly_reports'),
    path('goal_achievement_reports', views.goal_achievement_reports, name='goal_achievement_reports'),
    path('comparison_reports', views.comparison_reports, name='comparison_reports'),
]