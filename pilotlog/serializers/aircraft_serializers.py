from rest_framework import serializers

from ..models.aircraft import Aircraft


class AircraftSerializer(serializers.ModelSerializer):
    """
    Serializer for the Aircraft model.

    This serializer provides a comprehensive way to convert Aircraft model instances into JSON 
    format and vice-versa. It includes all fields of the Aircraft model, ensuring full data
    representation for API interactions. Use this serializer for operations involving the
    creation, retrieval, update, and deletion of aircraft records through the REST framework's
    views and viewsets.

    Attributes:
        Meta.model (Aircraft): The model that this serializer will serialize.
        Meta.fields (str): Specifies that all fields in the Aircraft model should be included in the 
                           serialized data.
    """

    class Meta:
        model = Aircraft
        fields = "__all__"
