from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('top-chart-get', views.topChartGet),
    path('jenis-chart-get', views.jenisChartGet)
]