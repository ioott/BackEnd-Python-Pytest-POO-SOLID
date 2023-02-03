import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    @staticmethod
    def import_data(path: str):
        prod_data = []
        if path.endswith(".json"):
            with open(path, mode="r") as file:
                prod_data = json.load(file)
                return prod_data

        else:
            raise ValueError("Arquivo inválido")
