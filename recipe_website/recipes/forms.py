from django import forms

class RecipeSearchForm(forms.Form):
    query = forms.CharField(required=False)
    cuisine = forms.CharField(required=False)
    excludeCuisine = forms.CharField(required=False)
    diet = forms.CharField(required=False)
    intolerances = forms.CharField(required=False)
    equipment = forms.CharField(required=False)
    includeIngredients = forms.CharField(required=False)
    excludeIngredients = forms.CharField(required=False)
    type = forms.CharField(required=False)
    image = forms.ImageField(required=False)

from django import forms
from .models import UserPreferences

# Options for cuisines, diets, and intolerances
CUISINE_OPTIONS = [
    ("", ""), ("African", "African"), ("Asian", "Asian"), ("American", "American"),
    ("British", "British"), ("Cajun", "Cajun"), ("Caribbean", "Caribbean"),
    ("Chinese", "Chinese"), ("Eastern European", "Eastern European"),
    ("European", "European"), ("French", "French"), ("German", "German"),
    ("Greek", "Greek"), ("Indian", "Indian"), ("Irish", "Irish"), ("Italian", "Italian"),
    ("Japanese", "Japanese"), ("Jewish", "Jewish"), ("Korean", "Korean"),
    ("Latin American", "Latin American"), ("Mediterranean", "Mediterranean"),
    ("Mexican", "Mexican"), ("Middle Eastern", "Middle Eastern"), ("Nordic", "Nordic"),
    ("Southern", "Southern"), ("Spanish", "Spanish"), ("Thai", "Thai"), ("Vietnamese", "Vietnamese")
]
DIET_OPTIONS = [
    ("", ""), ("Gluten Free", "Gluten Free"), ("Ketogenic", "Ketogenic"),
    ("Vegetarian", "Vegetarian"), ("Lacto-Vegetarian", "Lacto-Vegetarian"),
    ("Ovo-Vegetarian", "Ovo-Vegetarian"), ("Vegan", "Vegan"),
    ("Pescetarian", "Pescetarian"), ("Paleo", "Paleo"), ("Primal", "Primal")
]
INTOLERANCE_OPTIONS = [
    ("", ""), ("Dairy", "Dairy"), ("Egg", "Egg"), ("Gluten", "Gluten"),
    ("Grain", "Grain"), ("Peanut", "Peanut"), ("Seafood", "Seafood"),
    ("Sesame", "Sesame"), ("Shellfish", "Shellfish"), ("Soy", "Soy"),
    ("Sulfite", "Sulfite"), ("Tree Nut", "Tree Nut"), ("Wheat", "Wheat")
]

class PreferencesForm(forms.ModelForm):
    cuisines = forms.MultipleChoiceField(
        choices=CUISINE_OPTIONS,
        widget=forms.SelectMultiple(attrs={'class': 'form-dropdown'}),
        required=False
    )
    diets = forms.MultipleChoiceField(
        choices=DIET_OPTIONS,
        widget=forms.SelectMultiple(attrs={'class': 'form-dropdown'}),
        required=False
    )
    intolerances = forms.MultipleChoiceField(
        choices=INTOLERANCE_OPTIONS,
        widget=forms.SelectMultiple(attrs={'class': 'form-dropdown'}),
        required=False
    )

    class Meta:
        model = UserPreferences
        fields = ['cuisines', 'diets', 'intolerances']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.cuisines = ','.join(self.cleaned_data['cuisines'])
        instance.diets = ','.join(self.cleaned_data['diets'])
        instance.intolerances = ','.join(self.cleaned_data['intolerances'])
        if commit:
            instance.save()
        return instance
