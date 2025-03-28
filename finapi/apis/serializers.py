from rest_framework import serializers
from .models import CBNData

class CBNDataserializer(serializers.ModelSerializer):
    class Meta:
        model =CBNData
        fields = '__all__'