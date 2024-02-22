from django.test import TestCase
from pilotlog.models.aircraft import Aircraft
from pilotlog.serializers import AircraftSerializer


class AircraftSerializerTest(TestCase):
    def setUp(self):
        self.aircraft_attributes = {
            "aircraft_id": "A12345",
            "make": "Boeing",
            "model": "747",
            "year": "1980",
        }
        self.aircraft = Aircraft.objects.create(**self.aircraft_attributes)
        self.serializer = AircraftSerializer(instance=self.aircraft)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "aircraft_id",
                    "make",
                    "model",
                    "year",
                    "equipment_type",
                    "type_code",
                    "category",
                    "aircraft_class",
                    "gear_type",
                    "engine_type",
                    "complex",
                    "high_performance",
                    "pressurized",
                    "taa",
                ]
            ),
        )

    def test_make_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["make"], self.aircraft_attributes["make"])
