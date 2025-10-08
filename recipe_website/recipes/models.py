from django.db import models
from django.contrib.auth.models import User

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intolerances = models.TextField(blank=True, null=True)  # Stores selected intolerances as CSV
    cuisines = models.TextField(blank=True, null=True)      # Stores selected cuisines as CSV
    diets = models.TextField(blank=True, null=True)         # Stores selected diets as CSV

    def __str__(self):
        return f"{self.user.username}'s Preferences"
