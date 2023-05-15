from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = csv.DictReader(file)
            return list(data)


# CsvImporter.import_data("inventory_report/data/inventory.csv")