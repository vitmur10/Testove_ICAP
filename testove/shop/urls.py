from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
