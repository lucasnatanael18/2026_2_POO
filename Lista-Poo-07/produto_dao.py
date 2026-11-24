import json
from pathlib import Path
from produto import Produto


class ProdutoDAO:
    arquivo = Path(__file__).with_name("produtos.json")
    produtos = []
    proximo_id = 1

    @classmethod
    def _carregar(cls):
        """Carrega os produtos salvos no arquivo JSON."""
        if not cls.arquivo.exists():
            cls.produtos = []
            cls.proximo_id = 1
            return

        try:
            with cls.arquivo.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            dados = []

        cls.produtos = [
            Produto(
                item["id"],
                item["descricao"],
                item["preco"],
                item["estoque"],
                item["id_categoria"]
            )
            for item in dados
        ]
        cls.proximo_id = max((produto.id for produto in cls.produtos), default=0) + 1

    @classmethod
    def _salvar(cls):
        """Salva todos os produtos no arquivo JSON."""
        dados = [
            {
                "id": produto.id,
                "descricao": produto.descricao,
                "preco": produto.preco,
                "estoque": produto.estoque,
                "id_categoria": produto.id_categoria
            }
            for produto in cls.produtos
        ]

        temporario = cls.arquivo.with_suffix(".tmp")
        with temporario.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        temporario.replace(cls.arquivo)

    @classmethod
    def inserir(cls, produto):
        produto.id = cls.proximo_id
        cls.proximo_id += 1
        cls.produtos.append(produto)
        cls._salvar()

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
        cls._salvar()
        return True

    @classmethod
    def excluir(cls, id):
        produto = cls.listar_id(id)

        if produto is None:
            return False

        cls.produtos.remove(produto)
        cls._salvar()
        return True

    @classmethod
    def reajustar(cls, percentual):
        for produto in cls.produtos:
            produto.preco *= 1 + percentual / 100
        cls._salvar()


ProdutoDAO._carregar()
