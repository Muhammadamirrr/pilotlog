from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from pilotlog.models import Aircraft, Flight
from pilotlog.utils import export_model_to_csv


class Command(BaseCommand):
    """
    A Django management command to export Aircraft and Flight data to CSV files.

    This command retrieves all instances of Aircraft and Flight models from the database,
    and exports specified fields of these models to designated CSV files.
    """

    help = "Export data to CSV files"

    def handle(self, *args, **options):
        """
        The primary entry point for the management command.

        It defines the fields to be exported for each model, specifies the path for the output
        CSV files, and invokes the utility function to perform the export operation.
        """
        aircraft_fields = [
            "aircraft_id",
            "make",
            "model",
            "year",
            "category",
            "aircraft_class",
            "gear_type",
            "engine_type",
            "complex",
            "high_performance",
            "pressurized",
            "taa",
        ]
        flight_fields = [
            "date",
            "aircraft_id",
            "from_airport",
            "to_airport",
            "route",
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
        ]

        aircraft_csv_path = Path(settings.BASE_DIR) / "exports" / "aircraft_data.csv"
        flight_csv_path = Path(settings.BASE_DIR) / "exports" / "flight_data.csv"

        export_model_to_csv(Aircraft, aircraft_fields, aircraft_csv_path)
        export_model_to_csv(Flight, flight_fields, flight_csv_path)

        self.stdout.write(
            self.style.SUCCESS("Successfully exported data to CSV files.")
        )
