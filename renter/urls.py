from django.urls import include, path
from rest_framework import routers

from .views import RenterViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"renters", RenterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
