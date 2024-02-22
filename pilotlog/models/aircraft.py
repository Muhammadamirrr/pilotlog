from django.db import models


class Aircraft(models.Model):
    aircraft_id = models.CharField(max_length=36, primary_key=True)
    equipment_type = models.CharField(max_length=255, blank=True, null=True)
    type_code = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    aircraft_class = models.CharField(
        max_length=255, blank=True, null=True
    )  # 'class' is a reserved word so used this unlike format for csv file specified
    gear_type = models.CharField(max_length=255, blank=True, null=True)
    engine_type = models.CharField(max_length=255, blank=True, null=True)
    complex = models.BooleanField(default=False)
    high_performance = models.BooleanField(default=False)
    pressurized = models.BooleanField(default=False)
    taa = models.BooleanField(default=False)  # Technologically Advanced Aircraft

    def __str__(self):
        return f"{self.make} {self.model} ({self.aircraft_id})"
