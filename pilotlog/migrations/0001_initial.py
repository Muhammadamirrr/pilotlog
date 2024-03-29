# Generated by Django 5.0.2 on 2024-02-21 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aircraft",
            fields=[
                (
                    "aircraft_id",
                    models.CharField(max_length=36, primary_key=True, serialize=False),
                ),
                (
                    "equipment_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("type_code", models.CharField(blank=True, max_length=255, null=True)),
                ("year", models.CharField(blank=True, max_length=4, null=True)),
                ("make", models.CharField(max_length=255)),
                ("model", models.CharField(max_length=255)),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "aircraft_class",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("gear_type", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "engine_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("complex", models.BooleanField(default=False)),
                ("high_performance", models.BooleanField(default=False)),
                ("pressurized", models.BooleanField(default=False)),
                ("taa", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("guid", models.CharField(max_length=255, unique=True)),
                ("date", models.DateField()),
                (
                    "from_airport",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("to_airport", models.CharField(blank=True, max_length=255, null=True)),
                ("route", models.TextField(blank=True, null=True)),
                ("time_out", models.TimeField(blank=True, null=True)),
                ("time_off", models.TimeField(blank=True, null=True)),
                ("time_on", models.TimeField(blank=True, null=True)),
                ("time_in", models.TimeField(blank=True, null=True)),
                ("on_duty", models.TimeField(blank=True, null=True)),
                ("off_duty", models.TimeField(blank=True, null=True)),
                (
                    "total_time",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "pic",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "sic",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "night",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "solo",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "cross_country",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "nvg",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("nvgo_ops", models.IntegerField(blank=True, null=True)),
                (
                    "distance",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                ("day_takeoffs", models.IntegerField(blank=True, null=True)),
                ("day_landings_full_stop", models.IntegerField(blank=True, null=True)),
                ("night_takeoffs", models.IntegerField(blank=True, null=True)),
                (
                    "night_landings_full_stop",
                    models.IntegerField(blank=True, null=True),
                ),
                ("all_landings", models.IntegerField(blank=True, null=True)),
                (
                    "actual_instrument",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "simulated_instrument",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "hobbs_start",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "hobbs_end",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "tach_start",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "tach_end",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("holds", models.IntegerField(blank=True, null=True)),
                (
                    "dual_given",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "dual_received",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "simulated_flight",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "ground_training",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "instructor_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("instructor_comments", models.TextField(blank=True, null=True)),
                ("flight_review", models.BooleanField(default=False)),
                ("checkride", models.BooleanField(default=False)),
                ("ipc", models.BooleanField(default=False)),
                ("nvg_proficiency", models.BooleanField(default=False)),
                ("faa_6158", models.BooleanField(default=False)),
                ("pilot_comments", models.TextField(blank=True, null=True)),
                (
                    "aircraft",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flights",
                        to="pilotlog.aircraft",
                    ),
                ),
            ],
        ),
    ]
