import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @staticmethod
    def import_data(path: str, report_type: str):

        prod_data = []

        if path.endswith(".csv"):
            with open(path, "r") as file:
                all_products = csv.DictReader(file)
                for product in all_products:
                    prod_data.append(dict(product))

        elif path.endswith(".json"):
            with open(path, mode="r") as file:
                prod_data = json.load(file)

        elif path.endswith(".xml"):
            with open(path, mode="r") as file:
                file = file.read()
                file = xmltodict.parse(file)
                file = file['dataset']['record']

                for line in file:
                    prod_data.append(dict(line))

        if report_type == "simples":
            report = SimpleReport.generate(prod_data)
            return report
        else:
            report = CompleteReport.generate(prod_data)
            return report
