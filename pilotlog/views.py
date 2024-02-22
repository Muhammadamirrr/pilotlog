from rest_framework import viewsets

from .models import Aircraft, Flight
from .serializers import AircraftSerializer, FlightSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing aircraft instances.
    """

    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing flight instances.
    """

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
