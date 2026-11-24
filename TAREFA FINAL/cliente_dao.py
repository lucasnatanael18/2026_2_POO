import json
from pathlib import Path
from cliente import Cliente


class ClienteDAO:
    arquivo = Path(__file__).with_name("clientes.json")
    clientes = []
    proximo_id = 1

    @classmethod
    def _carregar(cls):
        """Carrega os clientes salvos no arquivo JSON."""
        if not cls.arquivo.exists():
            cls.clientes = []
            cls.proximo_id = 1
            return

        try:
            with cls.arquivo.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            dados = []

        cls.clientes = [
            Cliente(item["id"], item["nome"], item["email"], item["fone"])
            for item in dados
        ]
        cls.proximo_id = max((cliente.id for cliente in cls.clientes), default=0) + 1

    @classmethod
    def _salvar(cls):
        """Salva todos os clientes no arquivo JSON."""
        dados = [
            {
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email,
                "fone": cliente.fone
            }
            for cliente in cls.clientes
        ]

        temporario = cls.arquivo.with_suffix(".tmp")
        with temporario.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        temporario.replace(cls.arquivo)

    @classmethod
    def inserir(cls, cliente):
        cliente.id = cls.proximo_id
        cls.proximo_id += 1
        cls.clientes.append(cliente)
        cls._salvar()

    @classmethod
    def listar(cls):
        return list(cls.clientes)

    @classmethod
    def listar_id(cls, id):
        for cliente in cls.clientes:
            if cliente.id == id:
                return cliente
        return None

    @classmethod
    def atualizar(cls, cliente_atualizado):
        cliente = cls.listar_id(cliente_atualizado.id)

        if cliente is None:
            return False

        cliente.nome = cliente_atualizado.nome
        cliente.email = cliente_atualizado.email
        cliente.fone = cliente_atualizado.fone
        cls._salvar()
        return True

    @classmethod
    def excluir(cls, id):
        cliente = cls.listar_id(id)

        if cliente is None:
            return False

        cls.clientes.remove(cliente)
        cls._salvar()
        return True


ClienteDAO._carregar()
