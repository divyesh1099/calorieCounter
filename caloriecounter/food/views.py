from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    food_items = FoodItem.objects.all()
    context={
        'food_items': food_items,
    }
    return render(request, 'food/index.html', context)

def food_detail(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    context={
        'food_item': food_item,
    }
    return render(request, 'food/food_detail.html', context)