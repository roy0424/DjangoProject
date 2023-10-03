from django.urls import path
from . import views
from .views import verify_token

app_name = "food"

urlpatterns = [
    path('food/create/', views.create_food, name='create_food'),
    path('food/', views.get_all_food, name='get_all_food'),
    path('food/<int:food_id>/', views.get_food, name='get_specific_food'),
    path('food/<int:food_id>/update/', views.update_food, name='update_food'),
    path('food/<int:food_id>/delete/', views.delete_food, name='delete_food'),
    path('api/token/verify/', verify_token, name='token_verify'),
    path('brand/create/', views.create_brand, name='create_brand'),
    path('brand/', views.get_all_brand, name='get_all_brand'),
    path('brand/<int:brand_id>/', views.get_brand, name='get_specific_brand'),
    path('brand/<int:brand_id>/update/', views.update_brand, name='update_brand'),
    path('brand/<int:brand_id>/delete/', views.delete_brand, name='delete_brand'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/', views.get_all_category, name='get_all_category'),
    path('category/<int:category_id>/', views.get_category, name='get_specific_category'),
    path('category/<int:category_id>/update/', views.update_category, name='update_category'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
]
