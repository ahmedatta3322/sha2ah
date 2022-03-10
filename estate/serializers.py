from dataclasses import field
from rest_framework import serializers

from estate.models import Estate, Unit ,EstateType



class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"
class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
class EstateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= EstateType
        fields= '__all__'

