from django.urls import path
from . import views

urlpatterns = [
    path("payment/", views.InitiatePayment, name="initiatepayement"),
    path("payment/callback/", views.CompletePayment, name="completepayement"),
]