from django.urls import path

from accountsapp import views

urlpatterns = [
    path('update-userprofile/', views.UserProfileUpdateView.as_view()),
    path('user-address-create/', views.UserAddressCreateView.as_view()),
]