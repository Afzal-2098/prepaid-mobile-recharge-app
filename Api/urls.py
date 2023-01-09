from django.urls import path
from . import views

urlpatterns = [
    path("airtel/", views.AirtelPlanApi.as_view(), name="airtelplanapi"),
    path("airtel/<int:pk>", views.AirtelPlanApi.as_view(), name="airtelplanapi"),
]