from django.shortcuts import render
from .models import Transaction
from Api.models import *
import string
import random

'''I did not have Merchant account, so created a dummy payment and callback page''' 
''' created transaxtion data(transaction_id, merchant_id, checksum etc.)'''
'''these ids and data is created using string amd random module.'''


# Create your views here.
# initiates a payment page
def InitiatePayment(request):
    if request.method == "POST":
        data = request.POST.get('planid')
        phonenum = request.POST.get('phonenum')
        company_name = request.POST.get('companyname')
        if company_name == "Airtel":
            plandata = AirtelPlan.objects.filter(id=data)
        elif company_name == "Jio":
            plandata = JioPlan.objects.filter(id=data)
        else:
            plandata = ViPlan.objects.filter(id=data)

        context = {"paydata":plandata, "phone_num":phonenum}
    return render(request, "payments/pay.html", context)


# after successfull payment(dummy), this view stores transaction data in Transaction model 
def CompletePayment(request):
    if request.method == "POST":
        N = 10
        data = request.POST.get('iddata')
        phonenum = request.POST.get('phonenum')
        company_name = request.POST.get('companyname')
        if company_name == "Airtel":
            plandata = list(AirtelPlan.objects.filter(id=data).values())
        elif company_name == "Jio":
            plandata = list(JioPlan.objects.filter(id=data).values())
        else:
            plandata = list(ViPlan.objects.filter(id=data).values())
        
        amount = plandata[0]['price']
        company = plandata[0]['company']

        order_id = "".join(random.choices(string.ascii_lowercase+string.digits, k=N))
        transaction_id = "".join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase,k=N))
        bank_ref_id = "".join(random.choices(string.digits,k=N))
        merchant_id = "GVvZW0045768384024"
        bank_name = "State Bank of India"
        status = "Paid"
        message = "Your Payment has been successful."
        txnchacksum = "".join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase,k=N))

        context = {"paydata":plandata, "phone_num":phonenum, "message":message, "STATUS":status, "MID":merchant_id, "TXNID":transaction_id, "ORDERID":order_id, "BANKTXNID":bank_ref_id, "CHECKSUMHASH":txnchacksum, "BANKNAME":bank_name}

        trxn_obj = Transaction(made_by=phonenum, order_id=order_id, amount=amount, company=company, transaction_id=transaction_id, status=status, checksum=txnchacksum)
        trxn_obj.save()
    return render(request, "payments/callback.html", context)