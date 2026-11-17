from cliente import Cliente


class ClienteDAO:
    clientes = []
    proximo_id = 1

    @classmethod
    def inserir(cls, cliente):
        cliente.id = cls.proximo_id
        cls.proximo_id += 1
        cls.clientes.append(cliente)

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
        return True

    @classmethod
    def excluir(cls, id):
        cliente = cls.listar_id(id)

        if cliente is None:
            return False

        cls.clientes.remove(cliente)
        return True
