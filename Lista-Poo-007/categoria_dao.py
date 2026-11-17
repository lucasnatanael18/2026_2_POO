from categoria import Categoria


class CategoriaDAO:
    categorias = []
    proximo_id = 1

    @classmethod
    def inserir(cls, categoria):
        categoria.id = cls.proximo_id
        cls.proximo_id += 1
        cls.categorias.append(categoria)

    @classmethod
    def listar(cls):
        return list(cls.categorias)

    @classmethod
    def listar_id(cls, id):
        for categoria in cls.categorias:
            if categoria.id == id:
                return categoria
        return None

    @classmethod
    def atualizar(cls, categoria_atualizada):
        categoria = cls.listar_id(categoria_atualizada.id)

        if categoria is None:
            return False

        categoria.descricao = categoria_atualizada.descricao
        return True

    @classmethod
    def excluir(cls, id):
        categoria = cls.listar_id(id)

        if categoria is None:
            return False

        cls.categorias.remove(categoria)
        return True
