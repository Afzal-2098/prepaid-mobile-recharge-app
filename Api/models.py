from django.db import models

# Create your models here.

# Rest Api model
'''All the api model classes have common fields thats why inherited by abstract base class(CommonAttr)'''

class CommonAttr(models.Model):
    company = models.CharField(max_length=128)
    price = models.FloatField()
    data = models.FloatField()
    sms = models.PositiveIntegerField()
    validity = models.PositiveBigIntegerField()

    class Meta:
        abstract = True

class AirtelPlan(CommonAttr):
    company = models.CharField(max_length=128, default="Airtel", editable=False)

class JioPlan(CommonAttr):
    company = models.CharField(max_length=128, default="Jio", editable=False)

class ViPlan(CommonAttr):
    company = models.CharField(max_length=128, default="VI", editable=False)
    