from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CASTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'nim', views.NimViewSet)
router.register(r'prestasi', views.PrestasiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', CASTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('insert-nim/', views.insertNim),

]