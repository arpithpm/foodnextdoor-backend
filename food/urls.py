from django.urls import path
from food import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('cuisine/', views.CuisineListCreateView.as_view()),
    path('food-category/', views.FoodCategoryListCreateView.as_view()),
    path('chefs/', views.ChefListView.as_view()),

]

router = DefaultRouter()
router.register(r'payment-methods', views.PaymentMethodSupportedView
, basename='payment-methods')
urlpatterns = router.urls