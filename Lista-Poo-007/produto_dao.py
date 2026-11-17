from produto import Produto


class ProdutoDAO:
    produtos = []
    proximo_id = 1

    @classmethod
    def inserir(cls, produto):
        produto.id = cls.proximo_id
        cls.proximo_id += 1
        cls.produtos.append(produto)

    @classmethod
    def listar(cls):
        return list(cls.produtos)

    @classmethod
    def listar_id(cls, id):
        for produto in cls.produtos:
            if produto.id == id:
                return produto
        return None

    @classmethod
    def atualizar(cls, produto_atualizado):
        produto = cls.listar_id(produto_atualizado.id)

        if produto is None:
            return False

        produto.descricao = produto_atualizado.descricao
        produto.preco = produto_atualizado.preco
        produto.estoque = produto_atualizado.estoque
        produto.id_categoria = produto_atualizado.id_categoria
        return True

    @classmethod
    def excluir(cls, id):
        produto = cls.listar_id(id)

        if produto is None:
            return False

        cls.produtos.remove(produto)
        return True

    @classmethod
    def reajustar(cls, percentual):
        for produto in cls.produtos:
            produto.preco *= 1 + percentual / 100
