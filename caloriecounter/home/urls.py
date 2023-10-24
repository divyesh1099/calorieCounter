from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='home'
urlpatterns=[
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/', views.account, name='account'),
    path('account/edit-profile/', views.edit_profile, name='edit_profile'),
    path('account/confirm-delete/', views.delete_profile, name='delete_profile'),
]