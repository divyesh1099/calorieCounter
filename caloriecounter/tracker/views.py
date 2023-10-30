from datetime import date
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import *
from food.models import FoodItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, date 
from food.models import *
from .forms import *
from django.utils import timezone

# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        form = FoodLogForm(request.POST)
        if form.is_valid():
            food_log = form.save(commit=False)
            food_log.user = request.user
            food_log.save()
            return redirect('tracker')

    all_foods = FoodItem.objects.all()
    all_meal_types = MealType.objects.all()

    today = date.today()
    logs_today = FoodLog.objects.filter(user=request.user, date_time_consumed__date=today)
    
    total_calories_today = sum([log.food_item.calories * log.quantity for log in logs_today])

    context = {
        'all_foods': all_foods,
        'all_meal_types': all_meal_types,
        'logs_today': logs_today,
        'total_calories_today': total_calories_today,
    }
    return render(request, 'tracker/index.html', context)

def edit_log(request, log_id):
    log_instance = get_object_or_404(FoodLog, pk=log_id)

    if request.method == "POST":
        form = FoodLogForm(request.POST, instance=log_instance)
        if form.is_valid():
            form.save()
            return redirect('/tracker')
    else:
        form = FoodLogForm(instance=log_instance)
        meals=MealType.objects.all()
        foods=FoodItem.objects.all()
    context = {
        'form': form,
        'meals': meals,
        'foods': foods,
        }
    return render(request, 'tracker/edit_log.html', context)

@login_required
def delete_log(request, log_id):
    log_instance = get_object_or_404(FoodLog, pk=log_id)
    
    if request.method == "POST":
        log_instance.delete()
        return redirect('/tracker')

    context = {'log': log_instance}
    return render(request, 'tracker/confirm_delete.html', context)

@login_required
def add_food_log(request):
    if request.method == "POST":
        food_item = get_object_or_404(FoodItem, id=request.POST['food_item'])
        meal_type = get_object_or_404(MealType, id=request.POST['meal_type'])
        quantity = request.POST['quantity']

        # Create the food log
        FoodLog.objects.create(
            user=request.user,
            food_item=food_item,
            meal_type=meal_type,
            quantity=quantity,
            date_time_consumed=timezone.now()
        )
        
        messages.success(request, f'Successfully logged {food_item.name}')
        return redirect('/tracker')
    
@login_required
def daily_logs(request):
    today = date.today()
    logs = FoodLog.objects.filter(user=request.user, date_time_consumed__date=today)
    
    context = {
        'logs': logs,
        'date': today
    }
    return render(request, 'daily_logs.html', context)

@login_required
def log_detail(request, date_str):
    """
    Display the detailed food logs for a specific day.
    :param date_str: A string representing the date in the format 'YYYY-MM-DD'
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    logs = FoodLog.objects.filter(date=date_obj, user=request.user)

    context = {
        'date': date_obj,
        'logs': logs
    }

    return render(request, 'tracker/log_detail.html', context)