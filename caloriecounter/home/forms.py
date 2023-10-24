from django import forms
from .models import UserProfile, UserSettings

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture',
            'bio',
            'target_daily_calories',
            'target_protein',
            'target_carbs',
            'target_fat',
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us about yourself'}),
        }
        labels = {
            'profile_picture': 'Upload Profile Picture',
            'bio': 'About You',
            'target_daily_calories': 'Target Daily Calorie Intake',
            'target_protein': 'Target Protein (g)',
            'target_carbs': 'Target Carbohydrates (g)',
            'target_fat': 'Target Fat (g)',
        }

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = [
            'dietary_preference',
            'send_email_notifications',
            'theme_preference',
        ]
        labels = {
            'dietary_preference': 'Dietary Preference',
            'send_email_notifications': 'Send Email Notifications',
            'theme_preference': 'Theme Mode',
        }
