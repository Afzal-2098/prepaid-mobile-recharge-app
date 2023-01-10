from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Recharge.urls")),
    path("", include("Api.urls")),
    path("", include("payments.urls")),
]
