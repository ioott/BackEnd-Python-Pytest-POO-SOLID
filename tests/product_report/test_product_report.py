from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_prod = Product(
        id=1,
        nome_do_produto="massa de tomate",
        nome_da_empresa="trybe alimentos ltda",
        data_de_fabricacao="2022-09-09",
        data_de_validade="2023-04-09",
        numero_de_serie="333b33",
        instrucoes_de_armazenamento="Guarde bem",
    )
    expect = (
            "O produto massa de tomate"
            " fabricado em 2022-09-09"
            " por trybe alimentos ltda com validade"
            " até 2023-04-09"
            " precisa ser armazenado Guarde bem."
        )
    assert str(new_prod) == expect
