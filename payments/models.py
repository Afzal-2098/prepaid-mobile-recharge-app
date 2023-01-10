from django.db import models

# Create your models here.
'''this model is created in seperate app named payments app. this app has
all the business logic related to payment'''
'''stores data about all the transaction made on payment'''
'''data stores in this model for all api transactions'''

class Transaction(models.Model):
    made_by = models.CharField(max_length=128)
    order_id = models.CharField(unique=True, max_length=100)
    amount = models.PositiveIntegerField()
    company = models.CharField(max_length=64)
    transaction_id = models.CharField(max_length=64)
    made_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    checksum = models.CharField(max_length=100, null=True, blank=True)
