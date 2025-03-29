from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CBNDataViewSet, UserFinancialProfileViewSet, InvestmentTypeViewSet, investment_calculator

# Use SimpleRouter to prevent public root API exposure
router = SimpleRouter()
router.register(r'cbn-data', CBNDataViewSet)
router.register(r'user-financial-profile', UserFinancialProfileViewSet)
router.register(r'investment-type', InvestmentTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes registered API endpoints without exposing the root
    path('investment/', investment_calculator, name="investment-calculator"),  # Investment calculator page
]
