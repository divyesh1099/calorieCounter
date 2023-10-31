from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
import requests
from .secrets import FOOD_API_KEY

BASE_URL = "https://api.nal.usda.gov/fdc/v1"
API_KEY = FOOD_API_KEY
HEADERS = {
    "Content-Type": "application/json",
}

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
    
def add_food_item(request):
    context = {
        'api_status': None,
        'api_response': None,
        'api_error': None
    }
    if request.method == "POST":
        fdc_id = request.POST.get('fdc_id')
        endpoint = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}?api_key={API_KEY}"
        response = requests.get(endpoint)

        context['api_status'] = response.status_code
        if response.status_code != 200:
            context['api_error'] = 'Failed to fetch data from FDC. Please check the FDC ID and try again.'
            messages.error(request, context['api_error'])
            return render(request, 'food/add_food_item.html', context)
        try:
            data = response.json()
        except ValueError:
            messages.error(request, f"Error parsing API response. Status code: {response.status_code}. Response: {response.text}")
            return render(request, 'food/add_food_item.html')
        
        context['api_response'] = data

        nutrients_map = {
            "Energy": "calories",
            "Protein": "protein",
            "Carbohydrate, by difference": "total_carbohydrates",
            "Total lipid (fat)": "total_fats",
            "Fiber, total dietary": "dietary_fiber",
            "Sugars, total including NLEA": "sugars",
            "Starch": "starch",
            "Fatty acids, total saturated": "saturated_fats",
            "Fatty acids, total trans": "trans_fats",
            "Fatty acids, total monounsaturated": "monounsaturated_fats",
            "Fatty acids, total polyunsaturated": "polyunsaturated_fats",
            "Cholesterol": "cholesterol",
            "Sodium, Na": "sodium",
            "Potassium, K": "potassium",
            "Vitamin C, total ascorbic acid": "vitamin_c",
            "Iron, Fe": "iron",
        }

        food_data = {
            'name': data['description'],
            'description': data.get('additionalDescriptions', ''),
            'serving_size': data['foodPortions'][0]['gramWeight'] if 'foodPortions' in data and len(data['foodPortions']) > 0 else 0,
            'date_added': data.get('publishedDate', None),
            'last_updated': data.get('publishedDate', None),
            'image': data['images'][0]['url'] if 'images' in data else None
        }

        for nutrient in data['foodNutrients']:
            if nutrient['nutrient']['name'] in nutrients_map:
                field_name = nutrients_map[nutrient['nutrient']['name']]
                food_data[field_name] = nutrient['amount']

        FoodItem.objects.create(**food_data)
        messages.success(request, 'Food item added successfully!')
        return redirect('/food/add_food_item')

    return render(request, 'food/add_food_item.html', context)