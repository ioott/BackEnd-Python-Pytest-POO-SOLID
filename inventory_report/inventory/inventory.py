import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @staticmethod
    def import_data(path: str, report_type: str):

        if path.endswith(".csv"):
            prod_data = []
            with open(path, "r") as file:
                all_products = csv.DictReader(file)
                for product in all_products:
                    prod_data.append(dict(product))
        elif path.endswith(".json"):
            with open(path, mode="r") as file:
                prod_data = json.load(file)

        if report_type == "simples":
            report = SimpleReport.generate(prod_data)
            return report
        else:
            report = CompleteReport.generate(prod_data)
            return report
