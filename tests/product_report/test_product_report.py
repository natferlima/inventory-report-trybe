from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "produto1",
        "empresa1",
        "19/06/2022",
        "19/06/2024",
        123456789,
        "ao abrigo de luz")

    expected = (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )

    assert str(product) == expected
