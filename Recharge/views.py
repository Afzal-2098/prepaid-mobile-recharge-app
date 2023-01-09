from django.shortcuts import render
from Api.models import *

# Create your views here.
def Home(request):
    return render(request, "Recharge/home.html")

def Airtelplan(request):
    plans = Plan.objects.filter(company="airtel")
    context = {"plan_airtel":plans}
    return render(request, "Recharge/airtelviewplans.html", context)

def Recharge(request):
    return render(request, "Recharge/airtelrecharge.html")