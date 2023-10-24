from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile, UserSettings, UserStatistics, UserDailyLog
from .forms import UserProfileForm, UserSettingsForm
# Create your views here.
@login_required
def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

@login_required
def account(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Attempt to get UserProfile, UserSettings, and UserStatistics or create if they don't exist
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    user_statistics, created = UserStatistics.objects.get_or_create(user=request.user)

    context = {
        'user_profile': user_profile,
        'user_settings': user_settings,
        'user_statistics': user_statistics
    }
    
    return render(request, 'home/account.html', context)

@login_required
def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Attempt to get the user's profile or create if not exists
    userprofile, created = UserProfile.objects.get_or_create(user=request.user)
    usersettings, created = UserSettings.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        userprofile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        usersettings_form = UserSettingsForm(request.POST, instance=usersettings)

        if userprofile_form.is_valid() and usersettings_form.is_valid():
            userprofile_form.save()
            usersettings_form.save()
            messages.success(request, "Your profile and settings have been updated!")
            return redirect('account')
    else:
        userprofile_form = UserProfileForm(instance=userprofile)
        usersettings_form = UserSettingsForm(instance=usersettings)

    context = {
        'userprofile_form': userprofile_form,
        'usersettings_form': usersettings_form,
        'userprofile': userprofile
    }
    return render(request, 'home/edit_profile.html', context)

@login_required
def delete_profile(request):
    """ Delete the user's account and related data. """
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('home')
    return render(request, 'home/confirm_delete.html')