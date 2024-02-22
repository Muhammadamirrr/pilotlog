from django.test import TestCase
from pilotlog.models.aircraft import Aircraft
from pilotlog.models.flight import Flight
from datetime import date


class FlightModelTest(TestCase):
    def setUp(self):
        self.aircraft = Aircraft.objects.create(
            aircraft_id="123456", make="Boeing", model="747", year="1990"
        )
        self.flight = Flight.objects.create(
            guid="FL123",
            date=date.today(),
            aircraft=self.aircraft,
            from_airport="LAX",
            to_airport="JFK",
        )

    def test_flight_creation(self):
        self.assertTrue(isinstance(self.flight, Flight))
        self.assertEqual(self.flight.aircraft, self.aircraft)
        expected_str = f"Flight from LAX to JFK on {self.flight.date}"
        self.assertEqual(self.flight.__str__(), expected_str)
