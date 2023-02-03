import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):

    @staticmethod
    def import_data(path: str):
        prod_data = []
        if path.endswith(".csv"):
            with open(path, "r") as file:
                all_products = csv.DictReader(file)
                for product in all_products:
                    prod_data.append(dict(product))

            return prod_data

        else:
            raise ValueError("Arquivo inválido")
