from service import Service


def ler_texto(mensagem):
    return input(mensagem).strip()


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_float(mensagem):
    while True:
        try:
            valor = input(mensagem).strip().replace(",", ".")
            return float(valor)
        except ValueError:
            print("Digite um número válido.")


def menu():
    print("\n========== SISTEMA DE COMÉRCIO ELETRÔNICO ==========")
    print("CLIENTES")
    print("1 - Inserir cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Excluir cliente")
    print("\nCATEGORIAS")
    print("5 - Inserir categoria")
    print("6 - Listar categorias")
    print("7 - Atualizar categoria")
    print("8 - Excluir categoria")
    print("\nPRODUTOS")
    print("9 - Inserir produto")
    print("10 - Listar produtos")
    print("11 - Atualizar produto")
    print("12 - Excluir produto")
    print("13 - Reajustar preços dos produtos")
    print("\n0 - Finalizar")
    return ler_int("Escolha uma opção: ")


def cliente_inserir():
    print("\n--- Cadastro de cliente ---")
    nome = ler_texto("Nome: ")
    email = ler_texto("E-mail: ")
    fone = ler_texto("Fone: ")
    Service.cliente_inserir(nome, email, fone)
    print("Cliente cadastrado com sucesso.")


def cliente_listar():
    clientes = Service.cliente_listar()
    print("\n--- Clientes cadastrados ---")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(cliente)


def cliente_atualizar():
    id = ler_int("ID do cliente: ")
    if Service.cliente_listar_id(id) is None:
        print("Cliente não encontrado.")
        return

    nome = ler_texto("Novo nome: ")
    email = ler_texto("Novo e-mail: ")
    fone = ler_texto("Novo fone: ")

    if Service.cliente_atualizar(id, nome, email, fone):
        print("Cliente atualizado com sucesso.")
    else:
        print("Não foi possível atualizar o cliente.")


def cliente_excluir():
    id = ler_int("ID do cliente: ")
    if Service.cliente_excluir(id):
        print("Cliente excluído com sucesso.")
    else:
        print("Cliente não encontrado.")


def categoria_inserir():
    print("\n--- Cadastro de categoria ---")
    descricao = ler_texto("Descrição: ")
    Service.categoria_inserir(descricao)
    print("Categoria cadastrada com sucesso.")


def categoria_listar():
    categorias = Service.categoria_listar()
    print("\n--- Categorias cadastradas ---")

    if not categorias:
        print("Nenhuma categoria cadastrada.")
        return

    for categoria in categorias:
        print(categoria)


def categoria_atualizar():
    id = ler_int("ID da categoria: ")
    if Service.categoria_listar_id(id) is None:
        print("Categoria não encontrada.")
        return

    descricao = ler_texto("Nova descrição: ")
    if Service.categoria_atualizar(id, descricao):
        print("Categoria atualizada com sucesso.")
    else:
        print("Não foi possível atualizar a categoria.")


def categoria_excluir():
    id = ler_int("ID da categoria: ")
    if Service.categoria_excluir(id):
        print("Categoria excluída com sucesso.")
    else:
        print("Categoria não encontrada.")


def produto_inserir():
    print("\n--- Cadastro de produto ---")
    categoria_listar()
    descricao = ler_texto("Descrição: ")
    preco = ler_float("Preço: ")
    estoque = ler_int("Estoque: ")
    id_categoria = ler_int("ID da categoria: ")

    if Service.produto_inserir(descricao, preco, estoque, id_categoria):
        print("Produto cadastrado com sucesso.")
    else:
        print("Dados inválidos. Verifique o preço, o estoque e o ID da categoria.")


def produto_listar():
    produtos = Service.produto_listar()
    print("\n--- Produtos cadastrados ---")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        categoria = Service.categoria_listar_id(produto.id_categoria)
        nome_categoria = categoria.descricao if categoria else "Categoria não encontrada"
        print(f"{produto} | Categoria: {nome_categoria}")


def produto_atualizar():
    id = ler_int("ID do produto: ")
    if Service.produto_listar_id(id) is None:
        print("Produto não encontrado.")
        return

    categoria_listar()
    descricao = ler_texto("Nova descrição: ")
    preco = ler_float("Novo preço: ")
    estoque = ler_int("Novo estoque: ")
    id_categoria = ler_int("Novo ID da categoria: ")

    if Service.produto_atualizar(id, descricao, preco, estoque, id_categoria):
        print("Produto atualizado com sucesso.")
    else:
        print("Dados inválidos. Verifique o preço, o estoque e o ID da categoria.")


def produto_excluir():
    id = ler_int("ID do produto: ")
    if Service.produto_excluir(id):
        print("Produto excluído com sucesso.")
    else:
        print("Produto não encontrado.")


def produto_reajustar():
    produto_listar()
    percentual = ler_float(
        "Percentual de reajuste ou promoção (use negativo para promoção): "
    )

    try:
        Service.produto_reajustar(percentual)
        print("Preços atualizados com sucesso.")
        produto_listar()
    except ValueError as erro:
        print(erro)


def main():
    while True:
        opcao = menu()

        if opcao == 1:
            cliente_inserir()
        elif opcao == 2:
            cliente_listar()
        elif opcao == 3:
            cliente_atualizar()
        elif opcao == 4:
            cliente_excluir()
        elif opcao == 5:
            categoria_inserir()
        elif opcao == 6:
            categoria_listar()
        elif opcao == 7:
            categoria_atualizar()
        elif opcao == 8:
            categoria_excluir()
        elif opcao == 9:
            produto_inserir()
        elif opcao == 10:
            produto_listar()
        elif opcao == 11:
            produto_atualizar()
        elif opcao == 12:
            produto_excluir()
        elif opcao == 13:
            produto_reajustar()
        elif opcao == 0:
            print("Aplicação finalizada.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
