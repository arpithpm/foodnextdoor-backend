from django.urls import path

from accountsapp import views

urlpatterns = [
    path('update-userprofile/', views.UserProfileUpdateView.as_view()),
]