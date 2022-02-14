from django.urls import include, path
from rest_framework import routers

from estate.views import EstateViewSet, UnitViewSet

router = routers.SimpleRouter()
router.register(r"units", UnitViewSet)

router.register(r'estates', EstateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]