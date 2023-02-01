from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @staticmethod
    def generate(prod_data: list[dict]):

        all_registers = [product["nome_da_empresa"] for product in prod_data]
        companies_count = Counter(all_registers)

        result_lines = []
        for company, qtt in companies_count.items():
            result = f'- {company}: {qtt}\n'
            result_lines.append(result)

        result_lines = ''.join(result_lines)
        return (
            f'{SimpleReport.generate(prod_data)}\n'
            f'Produtos estocados por empresa:\n'
            f'{result_lines}'
        )
