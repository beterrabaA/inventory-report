from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        import_typer = {
            'csv': CsvImporter,
            'json': JsonImporter,
            'xml': XmlImporter
            }

        if report_type == "simples":
            return SimpleReport.generate(
                import_typer[path.split('.')[-1]].import_data(path))
        elif report_type == "completo":
            return CompleteReport.generate(
                import_typer[path.split('.')[-1]].import_data(path)
            )
        else:
            raise ValueError("Formato inválido")
