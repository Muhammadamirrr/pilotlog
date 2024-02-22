from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AircraftViewSet, FlightViewSet

router = DefaultRouter()
router.register(r"aircraft", AircraftViewSet)
router.register(r"flights", FlightViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
