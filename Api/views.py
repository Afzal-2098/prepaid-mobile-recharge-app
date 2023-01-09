from rest_framework.views import APIView
from .models import Plan
from .serializers import PlanSerializer
from rest_framework.response import Response
from rest_framework import status

class AirtelPlanApi(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            plans = Plan.objects.get(pk=pk)
            plan_serializer = PlanSerializer(plans)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)
        else:
            plans = Plan.objects.filter(company='airtel')
            plan_serializer = PlanSerializer(plans, many=True)
            return Response(plan_serializer.data, status=status.HTTP_200_OK)