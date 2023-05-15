from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            json_data = file.read()
            json_list = JsonImporter.json_to_dict(json_data)
            return json_list
        
    @staticmethod
    def json_to_dict(data):
        data = json.loads(data)
        return data
