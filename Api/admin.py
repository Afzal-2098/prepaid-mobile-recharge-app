from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Plan)
class PlanModelAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "price", "data", "sms", "validity"]