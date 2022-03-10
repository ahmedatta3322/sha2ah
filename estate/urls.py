from django.urls import include, path
from rest_framework import routers

from estate.views import EstateViewSet, UnitViewSet,EstateTypesViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"units", UnitViewSet)
router.register(r"estates", EstateViewSet)
router.register(r"estatetypes", EstateTypesViewSet)
urlpatterns = [
    path("", include(router.urls)),
  
]
