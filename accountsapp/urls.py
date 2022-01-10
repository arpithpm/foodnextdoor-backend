from django.urls import path

from accountsapp import views

urlpatterns = [
    # path('update-userprofile/<pk>', views.UserProfileUpdateView.as_view()),
    path('user-address-create/', views.UserAddressListCreateView.as_view()),
    path('user-address-create/<pk>', views.UserAddressGetUpdateDelete.as_view()),
]