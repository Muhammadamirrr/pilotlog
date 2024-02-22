from django.db import models


class AircraftQuerySet(models.QuerySet):
    def high_performance(self):
        return self.filter(high_performance=True)

    def by_make(self, make):
        return self.filter(make=make)


class AircraftManager(models.Manager):
    def get_queryset(self):
        return AircraftQuerySet(self.model, using=self._db)

    def high_performance(self):
        return self.get_queryset().high_performance()

    def by_make(self, make):
        return self.get_queryset().by_make(make)


class Aircraft(models.Model):
    """
    Represents an aircraft, detailing its specifications and characteristics.

    Attributes:
        aircraft_id (CharField): A unique identifier for the aircraft, acting as the primary key.
        equipment_type (CharField): The type of equipment on the aircraft, optional.
        type_code (CharField): A specific code representing the aircraft type, optional.
        year (CharField): The year of manufacture of the aircraft, optional.
        make (CharField): The manufacturer of the aircraft.
        model (CharField): The model of the aircraft.
        category (CharField): The category of the aircraft, optional.
        aircraft_class (CharField): The class of the aircraft, such as 'single-engine', optional.
                        Note: 'class' is a reserved word in Python, hence 'aircraft_class' is used.
        gear_type (CharField): The type of landing gear on the aircraft, optional.
        engine_type (CharField): The type of engine on the aircraft, optional.
        complex (BooleanField): Flag indicating if the aircraft is complex, based on criteria like
                                retractable gear.
        high_performance (BooleanField): Flag indicating if the aircraft is high performance,
                                         typically based on horsepower.
        pressurized (BooleanField): Flag indicating if the aircraft has a pressurized cabin.
        taa (BooleanField): Flag indicating if the aircraft is considered technologically advanced.
    """

    aircraft_id = models.CharField(max_length=36, primary_key=True)
    equipment_type = models.CharField(max_length=255, blank=True, null=True)
    type_code = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    aircraft_class = models.CharField(max_length=255, blank=True, null=True)
    gear_type = models.CharField(max_length=255, blank=True, null=True)
    engine_type = models.CharField(max_length=255, blank=True, null=True)
    complex = models.BooleanField(default=False)
    high_performance = models.BooleanField(default=False)
    pressurized = models.BooleanField(default=False)
    taa = models.BooleanField(default=False)

    objects = AircraftManager()

    def __str__(self):
        return f"{self.make} {self.model} ({self.aircraft_id})"
