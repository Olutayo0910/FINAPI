from django.shortcuts import render
from rest_framework import viewsets
from .models import CBNData, UserFinancialProfile, InvestmentType
from .serializers import CBNDataSerializer, UserFinancialProfileSerializer, InvestmentTypeSerializer

def home(request):
    return render(request, "home.html")

# Investment Calculator View (HTML Page)
def investment_calculator(request):
    investment_types = InvestmentType.objects.all()
    return render(request, 'investment.html', {'investment_types': investment_types})

# API Views
class CBNDataViewSet(viewsets.ModelViewSet):
    """Handles CBN Data CRUD operations."""
    queryset = CBNData.objects.all().order_by('-date')  # Show latest data first
    serializer_class = CBNDataSerializer

    def get_queryset(self):
        """Override to customize filtering if needed."""
        return super().get_queryset()


class UserFinancialProfileViewSet(viewsets.ModelViewSet):
    """Handles user financial profile operations."""
    queryset = UserFinancialProfile.objects.all()
    serializer_class = UserFinancialProfileSerializer


class InvestmentTypeViewSet(viewsets.ModelViewSet):
    """Handles investment type operations."""
    queryset = InvestmentType.objects.all()
    serializer_class = InvestmentTypeSerializer
