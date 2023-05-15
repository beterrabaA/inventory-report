from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = "Farinha"
    nome_da_empresa = "Dona Benta"
    data_de_fabricacao = "01-05-2021"
    data_de_validade = "02-06-2023"
    numero_de_serie = "X567H2"
    instrucoes_de_armazenamento = "ao abrigo de luz"

    produto = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert produto.id == 1
    assert produto.nome_do_produto == "Farinha"
    assert produto.nome_da_empresa == "Dona Benta"
    assert produto.data_de_fabricacao == "01-05-2021"
    assert produto.data_de_validade == "02-06-2023"
    assert produto.numero_de_serie == "X567H2"
    assert produto.instrucoes_de_armazenamento == "ao abrigo de luz"
