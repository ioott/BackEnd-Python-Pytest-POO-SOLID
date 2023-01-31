from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = "arroz"
    empresa = "Maricota"
    instrucoes = "ao abrigo do sol"

    product_instance = Product(1, produto, empresa, 2022, 2023, 12, instrucoes)

    assert product_instance.id == 1
    assert product_instance.nome_do_produto == "arroz"
    assert product_instance.nome_da_empresa == "Maricota"
    assert product_instance.data_de_fabricacao == "2022"
    assert product_instance.data_de_validade == "2023"
    assert product_instance.numero_de_serie == 12
    assert product_instance.instrucoes_de_armazenamento == "ao abrigo do sol"
