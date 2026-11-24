from cliente import Cliente
from categoria import Categoria
from produto import Produto
from cliente_dao import ClienteDAO
from categoria_dao import CategoriaDAO
from produto_dao import ProdutoDAO


class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        return ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO.excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        categoria = Categoria(0, descricao)
        CategoriaDAO.inserir(categoria)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        categoria = Categoria(id, descricao)
        return CategoriaDAO.atualizar(categoria)

    @staticmethod
    def categoria_excluir(id):
        return CategoriaDAO.excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        if CategoriaDAO.listar_id(id_categoria) is None or preco < 0 or estoque < 0:
            return False

        produto = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO.inserir(produto)
        return True

    @staticmethod
    def produto_listar():
        return ProdutoDAO.listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        if CategoriaDAO.listar_id(id_categoria) is None or preco < 0 or estoque < 0:
            return False

        produto = Produto(id, descricao, preco, estoque, id_categoria)
        return ProdutoDAO.atualizar(produto)

    @staticmethod
    def produto_excluir(id):
        return ProdutoDAO.excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        if percentual <= -100:
            raise ValueError("O percentual não pode ser igual ou inferior a -100%.")

        ProdutoDAO.reajustar(percentual)
