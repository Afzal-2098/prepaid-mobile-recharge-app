from django.contrib import admin
from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "made_by", "amount", "company", "transaction_id", "made_on", "status", "checksum"]