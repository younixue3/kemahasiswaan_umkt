from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'prestasi-mahasiswa', views.PrestasiMahasiswa)

urlpatterns = [
    path('', include(router.urls))
]