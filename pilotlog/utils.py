import csv


def export_model_to_csv(model, fields, csv_file_path):
    """
    Export data from a Django model to a CSV file.
    :param model: Django model class to export data from.
    :param fields: List of model field names to include in the CSV.
    :param csv_file_path: File path to write the CSV to.
    """
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(fields)  

        for instance in model.objects.all():
            writer.writerow([getattr(instance, field, "") for field in fields])
