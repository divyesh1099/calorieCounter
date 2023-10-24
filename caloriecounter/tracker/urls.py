from django.urls import path
from . import views
app_name='tracker'
urlpatterns=[
    path('', views.index, name='index'),
    path('add/', views.add_food_log, name='add_food_log'),
    path('daily/', views.daily_logs, name='daily_logs'),
    path('log/<str:date_str>/', views.log_detail, name='log_detail'),
    path('edit_log/<int:log_id>/', views.edit_log, name='edit_log'),
    path('delete_log/<int:log_id>/', views.delete_log, name='delete_log'),
]