from rest_framework.serializers import ModelSerializer

from .models import Renter


class RenterSerializer(ModelSerializer):
    class Meta:
        model = Renter
        fields = "__all__"
