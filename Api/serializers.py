from rest_framework import serializers
from .models import *

class AirtelPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirtelPlan
        fields = '__all__'

class JioPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = JioPlan
        fields = '__all__'

class ViPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViPlan
        fields = '__all__'