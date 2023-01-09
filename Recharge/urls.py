from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("View-plans/", views.Airtelplan, name="Airtelplan"),
    path("airtel-recharge/", views.Recharge, name="Airtelrecharge"),
]
