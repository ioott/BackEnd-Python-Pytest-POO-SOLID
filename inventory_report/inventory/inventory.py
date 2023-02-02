import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @staticmethod
    def import_data(path: str, report_type: str):
        if path.endswith(".csv"):
            prod_data = Inventory.csv(path)
        elif path.endswith(".json"):
            prod_data = Inventory.json(path)
        elif path.endswith(".xml"):
            prod_data = Inventory.xml(path)
        return Inventory.generate_report(prod_data, report_type)

    def csv(path):
        prod_data = []
        with open(path, "r") as file:
            all_products = csv.DictReader(file)
            for product in all_products:
                prod_data.append(dict(product))
        return prod_data

    def json(path):
        with open(path, mode="r") as file:
            prod_data = json.load(file)
            return prod_data

    def xml(path):
        prod_data = []
        with open(path, mode="r") as file:
            file = file.read()
            file = xmltodict.parse(file)
            file = file['dataset']['record']

            for line in file:
                prod_data.append(dict(line))
        return prod_data

    def generate_report(prod_data, report_type):
        if report_type == "simples":
            report = SimpleReport.generate(prod_data)
            return report
        else:
            report = CompleteReport.generate(prod_data)
            return report
