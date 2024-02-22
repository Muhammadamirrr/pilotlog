from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from pilotlog.models.aircraft import Aircraft


class AircraftViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.aircraft = Aircraft.objects.create(
            aircraft_id="A12345", make="Boeing", model="747", year="1980"
        )

    def test_get_aircraft_list(self):
        url = reverse("aircraft-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_aircraft_detail(self):
        url = reverse("aircraft-detail", kwargs={"pk": self.aircraft.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["make"], "Boeing")
