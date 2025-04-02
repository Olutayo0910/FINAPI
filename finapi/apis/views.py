from django.shortcuts import render, get_object_or_404
from datetime import timedelta, date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CBNData, UserFinancialProfile, InvestmentType
from .serializers import CBNDataSerializer, UserFinancialProfileSerializer, InvestmentTypeSerializer

def home(request):
    """Render the homepage with latest CBN rates and investment types."""
    investment_types = InvestmentType.objects.all()
    
    # Fetch latest CBN data
    latest_cbn_data = CBNData.objects.order_by('-date').first()

    # Fetch historical data (last 2 years)
    two_years_ago = date.today() - timedelta(days=730)
    historical_data = CBNData.objects.filter(date__gte=two_years_ago).order_by('date')

    history = [
        {
            "date": data.date.strftime('%Y-%m-%d'),
            "interest_rate": data.interest_rate,
            "inflation_rate": data.inflation_rate,
            "treasury_bill_rate": data.treasury_bill_rate,
            "bond_rate": data.bond_rate
        }
        for data in historical_data
    ]

    return render(request, "home.html", {
        "cbn_data": latest_cbn_data,
        "historical_data": history,
        "investment_types": investment_types
    })

def investment_calculator_page(request):
    # Handle your logic here and render the page
    return render(request, 'investment_calculator.html')

# API Views
class CBNDataViewSet(viewsets.ModelViewSet):
    queryset = CBNData.objects.all().order_by('-date')
    serializer_class = CBNDataSerializer

class UserFinancialProfileViewSet(viewsets.ModelViewSet):
    queryset = UserFinancialProfile.objects.all()
    serializer_class = UserFinancialProfileSerializer

class InvestmentTypeViewSet(viewsets.ModelViewSet):
    queryset = InvestmentType.objects.all()
    serializer_class = InvestmentTypeSerializer

@api_view(['GET', 'POST'])
def investment_calculator_api(request):
    if request.method == 'GET':
        return Response({
            "message": "Use POST to calculate investment returns.",
            "required_fields": ["user_id"],
            "example": {"user_id": 1}
        })

    elif request.method == 'POST':
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "User ID is required."}, status=400)

        user_profile = get_object_or_404(UserFinancialProfile, id=user_id)

        # Ensure we have CBN data
        cbn_data = CBNData.objects.order_by('-date').first()
        if not cbn_data:
            return Response({"error": "CBN data not available."}, status=400)

        # Ensure user has a valid investment budget
        P = user_profile.total_investment_budget or 0
        if P <= 0:
            return Response({"error": "Investment budget must be greater than zero."}, status=400)

        # Ensure investment duration is valid
        t = user_profile.preferred_investment_duration or 1
        try:
            t = int(t)
            if t <= 0:
                raise ValueError
        except ValueError:
            return Response({"error": "Invalid investment duration."}, status=400)

        # Define Investment Rates
        investment_rates = {
            "Treasury Bill": max(cbn_data.treasury_bill_rate or 0, 0),
            "Bond": max(cbn_data.bond_rate or 0, 0),
            "Fixed Deposit": max((cbn_data.interest_rate or 0) - 2, 0),
            "Mutual Fund": max((cbn_data.interest_rate or 0) + 1, 0),
            "Stock": max((cbn_data.inflation_rate or 0) + 5, 0),
        }

        # Calculate investment returns
        investment_options = []
        for investment_type, rate in investment_rates.items():
            A = P * (1 + rate / 100) ** t  # Compound interest formula
            investment_options.append({
                "investment_type": investment_type,
                "rate_applied": f"{rate:.2f}%",
                "expected_return": round(A, 2),
                "duration": f"{t} years"
            })

        return Response({
            "user": user_profile.full_name,
            "initial_budget": P,
            "investment_options": investment_options
        })
