from django.db import models

class CBNData(models.Model):
    date = models.DateField(auto_now_add=True)
    exchange_rate_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    inflation_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    treasury_bill_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bond_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update timestamp

    class Meta:
        ordering = ['-date']
        verbose_name = "CBN Data"
        verbose_name_plural = "CBN Data Entries"

    def __str__(self):
        return f"CBN Data - {self.date}"


class UserFinancialProfile(models.Model):
    INVESTMENT_GOALS = [
        ("short_term", "Short-Term (1-3 years)"),
        ("medium_term", "Medium-Term (3-7 years)"),
        ("long_term", "Long-Term (7+ years)"),
    ]
    
    RISK_TOLERANCE = [
        ("low", "Low Risk"),
        ("medium", "Medium Risk"),
        ("high", "High Risk"),
    ]

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    total_investment_budget = models.DecimalField(max_digits=12, decimal_places=2, help_text="Total investment budget in NGN")
    investment_goal = models.CharField(max_length=20, choices=INVESTMENT_GOALS)
    risk_tolerance = models.CharField(max_length=10, choices=RISK_TOLERANCE)
    preferred_investment_duration = models.IntegerField(help_text="Duration in years")

    def __str__(self):
        return f"{self.full_name} - {self.investment_goal} Investment"


class InvestmentType(models.Model):
    INVESTMENT_CHOICES = [
        ("treasury_bill", "Treasury Bill"),
        ("bond", "Government Bond"),
        ("fixed_deposit", "Fixed Deposit"),
        ("mutual_fund", "Mutual Fund"),
        ("stock", "Stock Market"),
    ]

    type_key = models.CharField(max_length=50, choices=INVESTMENT_CHOICES, unique=True)
    name = models.CharField(max_length=50)  # Store actual name
    description = models.TextField()

    class Meta:
        db_table = "investment_types"
        verbose_name = "Investment Type"
        verbose_name_plural = "Investment Types"

    def __str__(self):
        return self.name


class InvestmentCalculation(models.Model):
    user = models.ForeignKey(UserFinancialProfile, on_delete=models.CASCADE)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.CASCADE)
    cbn_data = models.ForeignKey(CBNData, on_delete=models.SET_NULL, null=True, blank=True)
    expected_return = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    calculation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.investment_type} Return on {self.calculation_date}"
