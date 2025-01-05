from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_recipes_view, name='search_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('account/', views.account_view, name='account'),
    path('detected_image/', views.detected_image_view, name='detected_image'), # other paths
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
