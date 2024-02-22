from django.test import TestCase
from pilotlog.models.aircraft import Aircraft
from pilotlog.models.flight import Flight
from pilotlog.serializers import AircraftSerializer, FlightSerializer


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


class FlightSerializerTest(TestCase):
    def setUp(self):
        # Create a related Aircraft instance for the ForeignKey relationship
        self.aircraft = Aircraft.objects.create(
            aircraft_id="B67890",
            make="Cessna",
            model="172",
            year="2005",
        )

        self.flight_attributes = {
            "guid": "FL123456",
            "date": "2023-01-01",
            "aircraft": self.aircraft,
            "from_airport": "LAX",
            "to_airport": "JFK",
        }
        self.flight = Flight.objects.create(**self.flight_attributes)
        self.serializer = FlightSerializer(instance=self.flight)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "guid",
                    "date",
                    "aircraft",
                    "from_airport",
                    "to_airport",
                    "total_time",
                    "pic",
                    "sic",
                    "night",
                    "solo",
                    "cross_country",
                    "nvg",
                    "nvgo_ops",
                    "distance",
                    "day_takeoffs",
                    "day_landings_full_stop",
                    "night_takeoffs",
                    "night_landings_full_stop",
                    "all_landings",
                    "actual_instrument",
                    "simulated_instrument",
                    "hobbs_start",
                    "hobbs_end",
                    "tach_start",
                    "tach_end",
                    "holds",
                    "dual_given",
                    "dual_received",
                    "simulated_flight",
                    "ground_training",
                    "instructor_name",
                    "instructor_comments",
                    "flight_review",
                    "checkride",
                    "ipc",
                    "nvg_proficiency",
                    "faa_6158",
                    "pilot_comments",
                    "time_on",
                    "time_in",
                    "time_out",
                    "off_duty",
                    "time_off",
                    "on_duty",
                    "route",
                    "id",
                ]
            ),
        )

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["guid"], self.flight_attributes["guid"])
        self.assertEqual(data["from_airport"], self.flight_attributes["from_airport"])
        self.assertEqual(data["to_airport"], self.flight_attributes["to_airport"])
