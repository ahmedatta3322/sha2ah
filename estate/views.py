from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from estate.models import Estate, Unit, EstateType
from estate.serializers import EstateSerializer, UnitSerializer, EstateTypeSerializer
from sha2ah.scopes import requires_scope
from rest_framework.decorators import api_view


# Create your views here.
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class EstateViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

    @requires_scope(
        "read:estates",
    )
    def list(self, request, *args, **kwargs):
        return super(EstateViewSet, self).list(request, *args, **kwargs)


class EstateTypesViewSet(viewsets.ModelViewSet):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer
