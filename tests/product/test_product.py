from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "produto1",
        "empresa1",
        "19/06/2022",
        "19/06/2024",
        123456789,
        "instuções de armazenamento")

    assert product.id == 1
    assert product.nome_do_produto == "produto1"
    assert product.nome_da_empresa == "empresa1"
    assert product.data_de_fabricacao == "19/06/2022"
    assert product.data_de_validade == "19/06/2024"
    assert product.numero_de_serie == 123456789
    assert product.instrucoes_de_armazenamento == "instuções de armazenamento"
