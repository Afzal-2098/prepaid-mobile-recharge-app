from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Airtel, Jio and VI apis
'''created using apiview, and only implemented get method we also can apply post, patch, delete methods'''
'''in these apis third party user only can retrieve data.'''

# Aitel plans api
class AirtelPlanApi(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            plans = AirtelPlan.objects.get(pk=pk)
            plan_serializer = AirtelPlanSerializer(plans)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)
        else:
            plans = AirtelPlan.objects.filter(company='airtel')
            plan_serializer = AirtelPlanSerializer(plans, many=True)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)


# Jio plans api
class JioPlanApi(APIView):
    def get(self,  request, pk=None, format=None):
        if pk is not None:
            plans = JioPlan.objects.get(pk=pk)
            plan_serializer = JioPlanSerializer(plans)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)
        else:
            plans = JioPlan.objects.filter(company='Jio')
            plan_serializer = JioPlanSerializer(plans, many=True)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)

# VI plans api
class ViPlanApi(APIView):
    def get(self,  request, pk=None, format=None):
        if pk is not None:
            plans = ViPlan.objects.get(pk=pk)
            plan_serializer = ViPlanSerializer(plans)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)
        else:
            plans = ViPlan.objects.filter(company='VI')
            plan_serializer = ViPlanSerializer(plans, many=True)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)