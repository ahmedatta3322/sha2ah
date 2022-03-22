from renter.models import Renter

from rest_framework import viewsets

from .serializer import RenterSerializer


# Create your views here.
class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
