from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(AirtelPlan)
class AirtelPlanModelAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "price", "data", "sms", "validity"]

@admin.register(JioPlan)
class JioPlanModelAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "price", "data", "sms", "validity"]

@admin.register(ViPlan)
class ViPlanModelAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "price", "data", "sms", "validity"]