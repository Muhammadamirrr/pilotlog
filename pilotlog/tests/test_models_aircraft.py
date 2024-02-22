from django.test import TestCase
from pilotlog.models.aircraft import Aircraft


class AircraftModelTest(TestCase):
    def setUp(self):
        self.aircraft = Aircraft.objects.create(
            aircraft_id="123456", make="Boeing", model="747", year="1990"
        )

    def test_aircraft_creation(self):
        self.assertTrue(isinstance(self.aircraft, Aircraft))
        self.assertEqual(self.aircraft.__str__(), "Boeing 747 (123456)")
