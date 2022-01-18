from django.urls import path
from food import views

urlpatterns = [
    # path('update-userprofile/', views.UserProfileUpdateView.as_view()),
    path('cuisine/', views.CuisineListCreateView.as_view()),
    path('food-category/', views.FoodCategoryListCreateView.as_view()),
    path('chefs/', views.ChefListView.as_view()),

]