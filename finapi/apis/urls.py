from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CBNDataViewSet

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'cbn-data', CBNDataViewSet)  # Registers API at /cbn-data/

urlpatterns = [
    path('', include(router.urls)),  # Includes all generated API endpoints
]
