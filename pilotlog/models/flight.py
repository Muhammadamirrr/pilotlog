from django.db import models

from . import Aircraft


class Flight(models.Model):
    guid = models.CharField(max_length=255, unique=True)
    date = models.DateField()
    aircraft = models.ForeignKey(
        Aircraft, on_delete=models.CASCADE, related_name="flights"
    )
    from_airport = models.CharField(max_length=255, blank=True, null=True)
    to_airport = models.CharField(max_length=255, blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    time_out = models.TimeField(blank=True, null=True)
    time_off = models.TimeField(blank=True, null=True)
    time_on = models.TimeField(blank=True, null=True)
    time_in = models.TimeField(blank=True, null=True)
    on_duty = models.TimeField(blank=True, null=True)
    off_duty = models.TimeField(blank=True, null=True)
    total_time = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    pic = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )  # Pilot in Command
    sic = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )  # Second in Command
    night = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cross_country = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    nvg = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )  # Night Vision Goggles
    nvgo_ops = models.IntegerField(blank=True, null=True)
    distance = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    day_takeoffs = models.IntegerField(blank=True, null=True)
    day_landings_full_stop = models.IntegerField(blank=True, null=True)
    night_takeoffs = models.IntegerField(blank=True, null=True)
    night_landings_full_stop = models.IntegerField(blank=True, null=True)
    all_landings = models.IntegerField(blank=True, null=True)
    actual_instrument = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    simulated_instrument = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    hobbs_start = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    hobbs_end = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    tach_start = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    tach_end = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    holds = models.IntegerField(blank=True, null=True)
    dual_given = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    dual_received = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    simulated_flight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    ground_training = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    instructor_name = models.CharField(max_length=255, blank=True, null=True)
    instructor_comments = models.TextField(blank=True, null=True)
    flight_review = models.BooleanField(default=False)
    checkride = models.BooleanField(default=False)
    ipc = models.BooleanField(default=False)  # Instrument Proficiency Check
    nvg_proficiency = models.BooleanField(default=False)
    faa_6158 = models.BooleanField(default=False)
    pilot_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Flight from {self.from_airport} to {self.to_airport} on {self.date}"
