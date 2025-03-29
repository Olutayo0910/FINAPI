from rest_framework import serializers
from .models import CBNData, UserFinancialProfile, InvestmentType

class CBNDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBNData
        fields = '__all__'
        read_only_fields = ['date', 'updated_at']  # Auto-generated fields


class UserFinancialProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFinancialProfile
        fields = '__all__'


class InvestmentTypeSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_key_display', read_only=True)  # Human-readable name

    class Meta:
        model = InvestmentType
        fields = ['id', 'type_key', 'type_display', 'name', 'description']
