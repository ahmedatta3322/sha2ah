from django.shortcuts import render
from rest_framework import viewsets

from estate.models import Estate, Unit
from estate.serializers import EstateSerializer, UnitSerializer


# Create your views here.
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
class EstateViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

