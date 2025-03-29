from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CBNDataViewSet, UserFinancialProfileViewSet, InvestmentTypeViewSet

# Create a router for API views
router = DefaultRouter()
router.register(r'cbn-data', CBNDataViewSet)
router.register(r'user-financial-profile', UserFinancialProfileViewSet)
router.register(r'investment-type', InvestmentTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),  # This includes API routes like /api/cbn-data/
]
