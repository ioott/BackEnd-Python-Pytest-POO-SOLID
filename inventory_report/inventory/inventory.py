import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @staticmethod
    def import_data(path: str, report_type: str):

        prod_data = []
        with open(path, "r") as file:
            all_products = csv.DictReader(file)
            for product in all_products:
                prod_data.append(dict(product))

        if report_type == "simples":
            report = SimpleReport.generate(prod_data)
            return report
        else:
            report = CompleteReport.generate(prod_data)
            return report
