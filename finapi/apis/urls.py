from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apis.views import (
    home,
    investment_calculator_page,
    investment_calculator_api,
    CBNDataViewSet,
    UserFinancialProfileViewSet,
    InvestmentTypeViewSet
)

router = SimpleRouter()
router.register(r'cbn-data', CBNDataViewSet)
router.register(r'user-financial-profile', UserFinancialProfileViewSet)
router.register(r'investment-type', InvestmentTypeViewSet)

urlpatterns = [
    path('', home, name="home"),  # Add this line to route '/' to home
    path('investment/', investment_calculator_page, name="investment-calculator-page"),
    path('investment-calculate/', investment_calculator_api, name="investment-calculator-api"),
    path('api/', include(router.urls)),  # Group API endpoints under /api/
]
