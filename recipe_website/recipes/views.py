from .yolo_model import load_model, detect_ingredients

yolo_model = load_model()  # Load the YOLO model once during server start


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'landing.html', {'username': request.user.username})
    return render(request, 'landing.html')  # Landing page for guests

import os
import uuid
from django.conf import settings
from django.utils.text import slugify
from .forms import RecipeSearchForm
from .yolo_model import detect_ingredients  # Assuming detect_ingredients is defined elsewhere


def search_recipes_view(request):
    options = {
        "meal_types": ["", "Main Course", "Dessert", "Appetizer", "Salad", "Snack"],
    }
    detected_image_path = None
    if request.method == 'POST':
        form = RecipeSearchForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            ingredients = None

            # Handling the uploaded image
            if 'image' in request.FILES:
                image = request.FILES['image']
                unique_name = slugify(image.name.split('.')[0]) + '_' + str(uuid.uuid4()) + '.' + image.name.split('.')[-1]
                image_path = os.path.join(settings.MEDIA_ROOT, unique_name)
                with open(image_path, 'wb+') as f:
                    for chunk in image.chunks():
                        f.write(chunk)

                # Detect ingredients using YOLO model
                ingredients, detected_image_path = detect_ingredients(image_path, yolo_model)
                if "Egg (Food)" in ingredients:
                    ingredients.append("eggs")
                    ingredients.remove("Egg (Food)")

            # Fetch user preferences
            user_preferences = UserPreferences.objects.filter(user=request.user).first()
            cuisines = user_preferences.cuisines if user_preferences else None
            diets = user_preferences.diets if user_preferences else None
            intolerances = user_preferences.intolerances if user_preferences else None

            # Determining if complex search criteria are present
            complex_search_criteria = any([
                data['query'],
                data['excludeIngredients'],
                data['type'],
                cuisines,
                diets,
                intolerances
            ])

            api_key = 'secret'

            if complex_search_criteria:
                # Use complexSearch for detailed search
                api_url = 'https://api.spoonacular.com/recipes/complexSearch'
                payload = {
                    'query': data['query'],
                    'equipment': data['equipment'],
                    'includeIngredients': ','.join(ingredients) if ingredients else data['includeIngredients'],
                    'excludeIngredients': data['excludeIngredients'],
                    'type': data['type'],
                    'instructionsRequired': data.get('instructionsRequired', True),
                    'fillIngredients': data.get('fillIngredients', True),
                    'addRecipeInformation': data.get('addRecipeInformation', True),
                    'addRecipeInstructions': data.get('addRecipeInstructions', True),
                    'cuisine': cuisines,
                    'diet': diets,
                    'intolerances': intolerances,
                    'apiKey': api_key,
                }
            else:
                # Use findByIngredients if ingredients are specified or if an image is uploaded
                combined_ingredients = ingredients if ingredients else []
                if data['includeIngredients']:
                    combined_ingredients += data['includeIngredients'].split(',')
                api_url = 'https://api.spoonacular.com/recipes/findByIngredients'
                payload = {
                    'ingredients': ','.join(combined_ingredients),
                    'number': 25,
                    'apiKey': api_key,
                }

            print(payload)
            # API Call
            response = requests.get(api_url, params=payload)
            if response.status_code != 200:
                print('error is here')
                return render(request, 'error.html', {'message': 'Failed to fetch recipes from Spoonacular API'})

            if api_url.endswith('findByIngredients'):
                recipes = response.json()  # findByIngredients returns a list
            else:
                recipes = response.json().get('results', [])  # complexSearch returns a dictionary with 'results'

            return render(request, 'results.html', {'recipes': recipes, 'options': options, 'detected_image_path': detected_image_path})
    else:
        form = RecipeSearchForm()

    return render(request, 'search.html', {'form': form, 'options': options, 'detected_image_path': detected_image_path})

import requests

def recipe_details(request, recipe_id):
    api_key = "c2438df9a242442386f95342c904265c"
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    response = requests.get(url, params={"apiKey": api_key})
    if response.status_code == 200:
        recipe = response.json()
        return render(request, "recipe_details.html", {"recipe": recipe})
    else:
        return render(request, "error.html", {"message": "Failed to fetch recipe details"})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserPreferences
from .forms import PreferencesForm


@login_required
def account_view(request):
    user_preferences, created = UserPreferences.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = PreferencesForm(request.POST, instance=user_preferences)
        if form.is_valid():
            form.save()
            return redirect("account")  # Redirect to the account page after saving
    else:
        form = PreferencesForm(instance=user_preferences)
    username = request.user.username
    context = {
        "form": form,
        "username": username
    }
    return render(request, "account.html", context)

def detected_image_view(request):
    image_path = request.GET.get('image_path')
    image_url = os.path.join(settings.MEDIA_URL, image_path)
    return render(request, 'detection.html', {'detected_image_path': image_url})
