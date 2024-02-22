from django.db import models

from . import Aircraft


class Flight(models.Model):
    """
    Represents a flight record, detailing various parameters and metrics associated with a flight.

    Attributes:
        guid (CharField): A unique identifier for the flight.
        date (DateField): The date of the flight.
        aircraft (ForeignKey): A reference to the Aircraft model, denoting the aircraft used
                               for this flight.
        from_airport (CharField): The departure airport, optional.
        to_airport (CharField): The destination airport, optional.
        route (TextField): The planned route for the flight, optional.
        time_out (TimeField): The time the aircraft started taxiing for departure, optional.
        time_off (TimeField): The takeoff time, optional.
        time_on (TimeField): The landing time, optional.
        time_in (TimeField): The time the aircraft stopped taxiing after landing, optional.
        on_duty (TimeField): The start time of the pilot's duty period, optional.
        off_duty (TimeField): The end time of the pilot's duty period, optional.
        total_time (DecimalField): The total duration of the flight, optional.
        pic (DecimalField): Time spent as Pilot in Command, optional.
        sic (DecimalField): Time spent as Second in Command, optional.
        night (DecimalField): Time flown during night hours, optional.
        solo (DecimalField): Solo flight time, optional.
        cross_country (DecimalField): Cross-country flight time, optional.
        nvg (DecimalField): Time using Night Vision Goggles, optional.
        nvgo_ops (IntegerField): Number of operations with NVG, optional.
        distance (DecimalField): Total distance flown, optional.
        day_takeoffs (IntegerField): Number of day takeoffs, optional.
        day_landings_full_stop (IntegerField): Number of day landings with full stop, optional.
        night_takeoffs (IntegerField): Number of night takeoffs, optional.
        night_landings_full_stop (IntegerField): Number of night landings with full stop, optional.
        all_landings (IntegerField): Total number of landings, optional.
        actual_instrument (DecimalField): Time in actual instrument conditions, optional.
        simulated_instrument (DecimalField): Time in simulated instrument conditions, optional.
        hobbs_start (DecimalField): Hobbs meter reading at the start of the flight, optional.
        hobbs_end (DecimalField): Hobbs meter reading at the end of the flight, optional.
        tach_start (DecimalField): Tachometer reading at the start of the flight, optional.
        tach_end (DecimalField): Tachometer reading at the end of the flight, optional.
        holds (IntegerField): Number of holds performed, optional.
        dual_given (DecimalField): Time giving dual instruction, optional.
        dual_received (DecimalField): Time receiving dual instruction, optional.
        simulated_flight (DecimalField): Time in simulated flight conditions, optional.
        ground_training (DecimalField): Time spent in ground training, optional.
        instructor_name (CharField): Name of the instructor, optional.
        instructor_comments (TextField): Comments from the instructor, optional.
        flight_review (BooleanField): Indicates if the flight was a flight review.
        checkride (BooleanField): Indicates if the flight was a checkride.
        ipc (BooleanField): Indicates if the flight included an Instrument Proficiency Check.
        nvg_proficiency (BooleanField): Indicates if the flight included NVG proficiency training.
        faa_6158 (BooleanField): Indicates if the flight adheres to FAA rule 6158.
        pilot_comments (TextField): Comments from the pilot, optional.
    """

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
    pic = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sic = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    night = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cross_country = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    nvg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
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
    ipc = models.BooleanField(default=False)
    nvg_proficiency = models.BooleanField(default=False)
    faa_6158 = models.BooleanField(default=False)
    pilot_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Flight from {self.from_airport} to {self.to_airport} on {self.date}"
