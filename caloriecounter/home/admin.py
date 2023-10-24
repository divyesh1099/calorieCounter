from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserSettings)
admin.site.register(UserStatistics)
admin.site.register(UserDailyLog)