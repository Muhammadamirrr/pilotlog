import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from pilotlog.models import Aircraft, Flight


class Command(BaseCommand):
    """
    A Django management command to import aircraft and flight data from a JSON file.

    This command reads data from a specified JSON file, corrects common JSON formatting issues,
    and then imports the data into the Aircraft and Flight models in the database. It handles
    the creation or updating of model instances based on the provided data.
    """

    help = "Import aircraft and flight data from a JSON file"

    def handle(self, *args, **options):
        """
        The entry point for the command.

        It opens the specified JSON file, attempts to correct common JSON issues,
        parses the JSON data, and imports it into the database.
        """
        # Path to JSON file
        data_file = Path(settings.BASE_DIR) / "data" / "import_pilotlog_mcc.json"

        try:
            with open(data_file, "r") as file:
                json_string = file.read()

                # Attempt to fix common JSON issues
                corrected_json_string = (
                    json_string.replace('\\"', '"').lstrip('"').rstrip('"')
                )

                data = json.loads(corrected_json_string)

                for record in data:
                    if record["table"] == "Aircraft":
                        Aircraft.objects.update_or_create(
                            aircraft_id=record["guid"],
                            defaults={
                                "make": record["meta"].get("Make", ""),
                                "model": record["meta"].get("Model", ""),
                                "year": record["meta"].get("Year", ""),
                                "category": record["meta"].get("Category", ""),
                                "aircraft_class": record["meta"].get("Class", ""),
                                "gear_type": record["meta"].get("GearType", ""),
                                "engine_type": record["meta"].get("EngineType", ""),
                                "complex": record["meta"].get("Complex", False),
                                "high_performance": record["meta"].get(
                                    "HighPerf", False
                                ),
                                "pressurized": record["meta"].get("Pressurized", False),
                                "taa": record["meta"].get("TAA", False),
                            },
                        )
                    elif record["table"] == "Flight":
                        aircraft, _ = Aircraft.objects.get_or_create(
                            aircraft_id=record["meta"]["AircraftCode"]
                        )
                        Flight.objects.update_or_create(
                            guid=record["guid"],
                            defaults={
                                "aircraft": aircraft,
                                "date": record["meta"].get("DateUTC", ""),
                                "from_airport": record["meta"].get("From", ""),
                                "to_airport": record["meta"].get("To", ""),
                                "route": record["meta"].get("Route", ""),
                                "time_out": record["meta"].get("TimeOut", None),
                                "time_off": record["meta"].get("TimeOff", None),
                                "time_on": record["meta"].get("TimeOn", None),
                                "time_in": record["meta"].get("TimeIn", None),
                                "total_time": record["meta"].get("TotalTime", 0),
                                "pic": record["meta"].get("PIC", 0),
                                "sic": record["meta"].get("SIC", 0),
                                "night": record["meta"].get("Night", 0),
                                "solo": record["meta"].get("Solo", 0),
                                "cross_country": record["meta"].get("CrossCountry", 0),
                                "nvg": record["meta"].get("NVG", 0),
                                "nvgo_ops": record["meta"].get("NVGOps", 0),
                                "distance": record["meta"].get("Distance", 0),
                                "day_takeoffs": record["meta"].get("DayTakeoffs", 0),
                                "day_landings_full_stop": record["meta"].get(
                                    "DayLandingsFullStop", 0
                                ),
                                "night_takeoffs": record["meta"].get(
                                    "NightTakeoffs", 0
                                ),
                                "night_landings_full_stop": record["meta"].get(
                                    "NightLandingsFullStop", 0
                                ),
                                "all_landings": record["meta"].get("AllLandings", 0),
                                "actual_instrument": record["meta"].get(
                                    "ActualInstrument", 0
                                ),
                                "simulated_instrument": record["meta"].get(
                                    "SimulatedInstrument", 0
                                ),
                                "hobbs_start": record["meta"].get("HobbsStart", 0),
                                "hobbs_end": record["meta"].get("HobbsEnd", 0),
                                "tach_start": record["meta"].get("TachStart", 0),
                                "tach_end": record["meta"].get("TachEnd", 0),
                                "holds": record["meta"].get("Holds", 0),
                                "dual_given": record["meta"].get("DualGiven", 0),
                                "dual_received": record["meta"].get("DualReceived", 0),
                                "simulated_flight": record["meta"].get(
                                    "SimulatedFlight", 0
                                ),
                                "ground_training": record["meta"].get(
                                    "GroundTraining", 0
                                ),
                                "instructor_name": record["meta"].get(
                                    "InstructorName", ""
                                ),
                                "instructor_comments": record["meta"].get(
                                    "InstructorComments", ""
                                ),
                                "flight_review": record["meta"].get(
                                    "FlightReview", False
                                ),
                                "checkride": record["meta"].get("Checkride", False),
                                "ipc": record["meta"].get("IPC", False),
                                "nvg_proficiency": record["meta"].get(
                                    "NVGProficiency", False
                                ),
                                "faa_6158": record["meta"].get("FAA6158", False),
                                "pilot_comments": record["meta"].get(
                                    "PilotComments", ""
                                ),
                            },
                        )

            self.stdout.write(
                self.style.SUCCESS("Successfully imported data from JSON.")
            )
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f"Error decoding JSON: {e}"))
