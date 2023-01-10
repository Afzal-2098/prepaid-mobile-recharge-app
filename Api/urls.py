from django.urls import path
from . import views

'''api links through which this party application can retrieve data'''
'''these are browsable apis so you can copy and paste following link in browser. it will show all the plans available'''

'''
http://127.0.0.1:8000/airtel/    ---->fetch all the data stored in database
http://127.0.0.1:8000/airtel/1   ---->fetch data item whose primary key is 1.

http://127.0.0.1:8000/jio/
http://127.0.0.1:8000/jio/2

http://127.0.0.1:8000/vi/
http://127.0.0.1:8000/vi/3

'''

urlpatterns = [
    path("airtel/", views.AirtelPlanApi.as_view(), name="airtelplanapi"),
    path("airtel/<int:pk>", views.AirtelPlanApi.as_view(), name="airtelplanapiid"),
    path("jio/", views.JioPlanApi.as_view(), name="jioplanapi"),
    path("jio/<int:pk>", views.JioPlanApi.as_view(), name="jioplanapiid"),
    path("vi/", views.ViPlanApi.as_view(), name="viplanapi"),
    path("vi/<int:pk>", views.ViPlanApi.as_view(), name="viplanapiid"),
]