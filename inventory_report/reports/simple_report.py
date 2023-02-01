from datetime import date


class SimpleReport:

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

        return (
            f'Data de fabricação mais antiga: {old_fact}\n'
            f'Data de validade mais próxima: {exp_dates}\n'
            f'Empresa com mais produtos: {max_company}'
        )
