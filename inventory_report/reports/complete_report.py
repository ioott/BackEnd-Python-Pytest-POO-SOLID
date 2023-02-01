from inventory_report.reports.simple_report import SimpleReport
from datetime import date
from collections import Counter


class CompleteReport(SimpleReport):

    @staticmethod
    def generate(prod_data: list[dict]):
        old_fact = min(product["data_de_fabricacao"] for product in prod_data)

        exp_dates = min(
            exp_date for product in prod_data
            for exp_date in [product["data_de_validade"]]
            if exp_date >= date.today().isoformat()
        )

        max_company = [product["nome_da_empresa"] for product in prod_data]
        max_company = max(set(max_company), key=max_company.count)

        all_registers = [product["nome_da_empresa"] for product in prod_data]
        companies_count = Counter(all_registers)

        result_lines = []
        for company, qtt in companies_count.items():
            result = f'- {company}: {qtt}\n'
            result_lines.append(result)

        result_lines = ''.join(result_lines)

        complete_report = (
            f'Data de fabricação mais antiga: {old_fact}\n'
            f'Data de validade mais próxima: {exp_dates}\n'
            f'Empresa com mais produtos: {max_company}\n'
            f'Produtos estocados por empresa:\n'
            f'{result_lines}'
        )

        return complete_report
