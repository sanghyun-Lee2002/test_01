from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('api/accounts', RegisterView.as_view(), name='register'),
    path('api/accounts/login', LoginView.as_view(), name='login'),
    path('api/accounts/<str:username>', ProfileView.as_view(), name='profile'),
]


# from django.contrib import admin
# from django.urls import path, include
# from . import views

# app_name = "accounts"
# urlpatterns = [
#    path("", views.signup),
#    path("forms",views.m)
# ]
