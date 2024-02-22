from rest_framework import serializers

from ..models.flight import Flight


class FlightSerializer(serializers.ModelSerializer):
    """
    Serializer for the Flight model.

    This serializer is designed to convert Flight model instances into JSON format and back,
    facilitating easy data exchange between the server and clients in API calls. It serializes
    all fields of the Flight model, ensuring a comprehensive representation of flight data for
    API consumers.

    The serializer can be utilized in views and viewsets provided by Django REST Framework to handle
    standard CRUD operations on flight records, as well as any custom business logic requiring
    flight data manipulation or presentation.

    Attributes:
        Meta.model (Flight): Specifies the model related to this serializer.
        Meta.fields (str): Indicates that all fields in the Flight model are included in the
                           serialization and deserialization processes.
    """

    class Meta:
        model = Flight
        fields = "__all__"
