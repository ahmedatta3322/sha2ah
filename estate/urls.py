from django.urls import include, path
from rest_framework import routers

from estate.views import EstateViewSet, UnitViewSet, EstateTypesViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"units", UnitViewSet)
router.register(r"estates", EstateViewSet)
router.register(r"estatetypes", EstateTypesViewSet)
# router.register(r"estates/show/<int:pk>", EstateViewSet.retrieve)
urlpatterns = [
    path("", include(router.urls)),
]
