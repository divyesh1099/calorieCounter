from django.urls import path
from . import views
app_name='food'
urlpatterns=[
    path('', views.index, name='index'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
]