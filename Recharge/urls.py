from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("phone-number/", views.PhoneNumber, name="phonenumber"),
    path("View-plans/", views.Airtelplan, name="Airtelplan"),
    path("airtel-recharge/", views.Airtelrecharge, name="Airtelrecharge"),
    path("JioView-plans/", views.Jioplan, name="jioplan"),
    path("jio-recharge/", views.Jiorecharge, name="jiorecharge"),
    path("ViView-plans/", views.Viplan, name="viplan"),
    path("vi-recharge/", views.Virecharge, name="virecharge"),
]
