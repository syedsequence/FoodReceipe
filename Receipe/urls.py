# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category-list'),  # GET, POST
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),  # GET, PUT, PATCH, DELETE

    # SubCategory URLs
    path('subcategories/', views.subcategory_list, name='subcategory-list'),  # GET, POST
    path('subcategories/<int:pk>/', views.subcategory_detail, name='subcategory-detail'),  # GET, PUT, PATCH, DELETE

    # Receipe URLs
    path('receipes/', views.receipe_list, name='receipe-list'),  # GET, POST
    path('receipes/<int:pk>/', views.receipe_detail, name='receipe-detail'),  # GET, PUT, PATCH, DELETE

    # Ingredient URLs
    path('ingredients/', views.ingredient_list, name='ingredient-list'),  # GET, POST
    path('ingredients/<int:pk>/', views.ingredient_detail, name='ingredient-detail'),  # GET, PUT, PATCH, DELETE
]
