from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(path)
        root = tree.getroot()

        data = []
        for child in root:
            item = {}
            for subchild in child:
                item[subchild.tag] = subchild.text
            data.append(item)
        return data