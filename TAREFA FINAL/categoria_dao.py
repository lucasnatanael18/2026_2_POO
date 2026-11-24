import json
from pathlib import Path
from categoria import Categoria


class CategoriaDAO:
    arquivo = Path(__file__).with_name("categorias.json")
    categorias = []
    proximo_id = 1

    @classmethod
    def _carregar(cls):
        """Carrega as categorias salvas no arquivo JSON."""
        if not cls.arquivo.exists():
            cls.categorias = []
            cls.proximo_id = 1
            return

        try:
            with cls.arquivo.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            dados = []

        cls.categorias = [
            Categoria(item["id"], item["descricao"])
            for item in dados
        ]
        cls.proximo_id = max((categoria.id for categoria in cls.categorias), default=0) + 1

    @classmethod
    def _salvar(cls):
        """Salva todas as categorias no arquivo JSON."""
        dados = [
            {"id": categoria.id, "descricao": categoria.descricao}
            for categoria in cls.categorias
        ]

        temporario = cls.arquivo.with_suffix(".tmp")
        with temporario.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        temporario.replace(cls.arquivo)

    @classmethod
    def inserir(cls, categoria):
        categoria.id = cls.proximo_id
        cls.proximo_id += 1
        cls.categorias.append(categoria)
        cls._salvar()

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
        cls._salvar()
        return True

    @classmethod
    def excluir(cls, id):
        categoria = cls.listar_id(id)

        if categoria is None:
            return False

        cls.categorias.remove(categoria)
        cls._salvar()
        return True


CategoriaDAO._carregar()
