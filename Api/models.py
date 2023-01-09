from django.db import models

# Create your models here.
class Plan(models.Model):
    company = models.CharField(max_length=128)
    price = models.FloatField()
    data = models.FloatField()
    sms = models.PositiveIntegerField()
    validity = models.PositiveBigIntegerField()