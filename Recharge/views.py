from django.shortcuts import render
from Api.models import *

# Create your views here.
# Home page view
def Home(request):
    return render(request, "Recharge/home.html")

# handles phone number after plan selection.
def PhoneNumber(request):
    if request.method == "POST":
        planid = request.POST.get("planid")
        company_name = request.POST.get("companyname")
        if company_name == "Airtel":
            plandata = AirtelPlan.objects.filter(id=planid)
        elif company_name == "Jio":
            plandata = JioPlan.objects.filter(id=planid)
        else:
            plandata = ViPlan.objects.filter(id=planid)
        context = {"plandata":plandata}
    return render(request, "Recharge/phonenumber.html", context)


# Airtel plan view, which interacts with Airtel Plan RestApi
def Airtelplan(request):
    if request.method == "POST":
        phone_num = request.POST.get("monumber")
        amount = request.POST.get("amount")
        if phone_num is not None and amount is not "":
            mob_num = phone_num
            plan_amount = amount
            querydata = list(AirtelPlan.objects.filter(price=plan_amount))
            plans = querydata
            if querydata == []:
                msg = "There is no plan available for this amount."
                return render(request, "Recharge/airtelviewplans.html",{"phone_num":mob_num, "amount":plan_amount, "msg":msg})
            else:
                return render(request, "Recharge/airtelviewplans.html",{"plan_airtel":plans, "phone_num":mob_num, "amount":plan_amount})
            
        elif phone_num is not None:
            mob_num = phone_num
            plans = AirtelPlan.objects.all()
            return render(request, "Recharge/airtelviewplans.html", {"plan_airtel":plans, "phone_num":mob_num})
        
    plans = AirtelPlan.objects.all()
    context = {"plan_airtel":plans}
    return render(request, "Recharge/airtelviewplans.html", context)

# renders airtel recharge page
def Airtelrecharge(request):
    return render(request, "Recharge/airtelrecharge.html")


# Jio plan view, intracts with JioPlanApi
def Jioplan(request):
    if request.method == "POST":
        phone_num = request.POST.get("monumber")
        amount = request.POST.get("amount")
        if phone_num is not None and amount is not "":
            mob_num = phone_num
            plan_amount = amount
            querydata = list(JioPlan.objects.filter(price=plan_amount))
            plans = querydata
            if querydata == []:
                msg = "There is no plan available for this amount."
                return render(request, "Recharge/jioviewplans.html",{"phone_num":mob_num, "amount":plan_amount, "msg":msg})
            else:
                return render(request, "Recharge/jioviewplans.html",{"plan_jio":plans, "phone_num":mob_num, "amount":plan_amount})

        elif phone_num is not None:
            mob_num = phone_num
            plans = JioPlan.objects.all()
            return render(request, "Recharge/jioviewplans.html", {"plan_jio":plans, "phone_num":mob_num})

    plans = JioPlan.objects.all()
    context = {"plan_jio":plans}
    return render(request, "Recharge/jioviewplans.html", context)

# renders jio recharge page
def Jiorecharge(request):
    return render(request, "Recharge/jiorecharge.html")


# VI Plan view, Intracts with ViPlanApi
def Viplan(request):
    if request.method == "POST":
        phone_num = request.POST.get("monumber")
        amount = request.POST.get("amount")
        if phone_num is not None and amount is not "":
            mob_num = phone_num
            plan_amount = amount
            querydata = list(ViPlan.objects.filter(price=plan_amount))
            plans = querydata
            if querydata == []:
                msg = "There is no plan available for this amount."
                return render(request, "Recharge/viviewplans.html",{"phone_num":mob_num, "amount":plan_amount, "msg":msg})
            else:
                return render(request, "Recharge/viviewplans.html",{"plan_vi":plans, "phone_num":mob_num, "amount":plan_amount})

        elif phone_num is not None:
            mob_num = phone_num
            plans = ViPlan.objects.all()
            return render(request, "Recharge/viviewplans.html", {"plan_vi":plans, "phone_num":mob_num})

    plans = ViPlan.objects.all()
    context = {"plan_vi":plans}
    return render(request, "Recharge/viviewplans.html", context)

# renders vi recharge page
def Virecharge(request):
    return render(request, "Recharge/virecharge.html")