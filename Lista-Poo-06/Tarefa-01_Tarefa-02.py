import json
import os

class Cliente:
    def __init__(self, id, n, e, f):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__fone = f

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def ToString(self):
        return (
            f"ID: {self.__id}\n"
            f"Nome: {self.__nome}\n"
            f"E-mail: {self.__email}\n"
            f"Telefone: {self.__fone}"
        )

class ClienteDAO:
    objetos = []
    arquivo = "clientes.json"

    @classmethod
    def Inserir(cls, obj):
        if obj.get_id() <= 0:
            obj.set_id(cls.ProximoId())

        if cls.Listar_Id(obj.get_id()) is not None:
            print("Erro: já existe um cliente com esse ID.")
            return False

        cls.objetos.append(obj)
        cls.Salvar()
        print("Cliente cadastrado com sucesso!")
        return True

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id):
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cliente = cls.Listar_Id(obj.get_id())

        if cliente is None:
            print("Cliente não encontrado.")
            return False

        cliente.set_nome(obj.get_nome())
        cliente.set_email(obj.get_email())
        cliente.set_fone(obj.get_fone())

        cls.Salvar()
        print("Cliente atualizado com sucesso!")
        return True

    @classmethod
    def Excluir(cls, obj):
        cliente = cls.Listar_Id(obj.get_id())

        if cliente is None:
            print("Cliente não encontrado.")
            return False

        cls.objetos.remove(cliente)
        cls.Salvar()
        print("Cliente excluído com sucesso!")
        return True

    @classmethod
    def ProximoId(cls):
        if not cls.objetos:
            return 1

        return max(obj.get_id() for obj in cls.objetos) + 1

    @classmethod
    def Abrir(cls):
        if not os.path.exists(cls.arquivo):
            cls.objetos = []
            return

        try:
            with open(cls.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            cls.objetos = []

            for item in dados:
                cliente = Cliente(
                    item["id"],
                    item["nome"],
                    item["email"],
                    item["fone"]
                )
                cls.objetos.append(cliente)

            print(f"{len(cls.objetos)} cliente(s) carregado(s).")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Erro ao ler o arquivo JSON.")
            cls.objetos = []

        except OSError as erro:
            print(f"Erro ao abrir o arquivo: {erro}")
            cls.objetos = []

    @classmethod
    def Salvar(cls):
        dados = []

        for obj in cls.objetos:
            dados.append({
                "id": obj.get_id(),
                "nome": obj.get_nome(),
                "email": obj.get_email(),
                "fone": obj.get_fone()
            })

        try:
            with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(
                    dados,
                    arquivo,
                    ensure_ascii=False,
                    indent=4
                )
        except OSError as erro:
            print(f"Erro ao salvar os dados: {erro}")


# ==================================================
# TAREFA 2 - CLASSE UI
# ==================================================

import json
import os

class Cliente:
    def __init__(self, id, n, e, f):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__fone = f

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def ToString(self):
        return (
            f"ID: {self.__id}\n"
            f"Nome: {self.__nome}\n"
            f"E-mail: {self.__email}\n"
            f"Telefone: {self.__fone}"
        )

class ClienteDAO:
    objetos = []
    arquivo = "clientes.json"

    @classmethod
    def Inserir(cls, obj):
        if obj.get_id() <= 0:
            obj.set_id(cls.ProximoId())

        if cls.Listar_Id(obj.get_id()) is not None:
            print("Erro: já existe um cliente com esse ID.")
            return False

        cls.objetos.append(obj)
        cls.Salvar()
        print("Cliente cadastrado com sucesso!")
        return True

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id):
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cliente = cls.Listar_Id(obj.get_id())

        if cliente is None:
            print("Cliente não encontrado.")
            return False

        cliente.set_nome(obj.get_nome())
        cliente.set_email(obj.get_email())
        cliente.set_fone(obj.get_fone())

        cls.Salvar()
        print("Cliente atualizado com sucesso!")
        return True

    @classmethod
    def Excluir(cls, obj):
        cliente = cls.Listar_Id(obj.get_id())

        if cliente is None:
            print("Cliente não encontrado.")
            return False

        cls.objetos.remove(cliente)
        cls.Salvar()
        print("Cliente excluído com sucesso!")
        return True

    @classmethod
    def ProximoId(cls):
        if not cls.objetos:
            return 1

        return max(obj.get_id() for obj in cls.objetos) + 1

    @classmethod
    def Abrir(cls):
        if not os.path.exists(cls.arquivo):
            cls.objetos = []
            return

        try:
            with open(cls.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            cls.objetos = []

            for item in dados:
                cliente = Cliente(
                    item["id"],
                    item["nome"],
                    item["email"],
                    item["fone"]
                )
                cls.objetos.append(cliente)

            print(f"{len(cls.objetos)} cliente(s) carregado(s).")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Erro ao ler o arquivo JSON.")
            cls.objetos = []

        except OSError as erro:
            print(f"Erro ao abrir o arquivo: {erro}")
            cls.objetos = []

    @classmethod
    def Salvar(cls):
        dados = []

        for obj in cls.objetos:
            dados.append({
                "id": obj.get_id(),
                "nome": obj.get_nome(),
                "email": obj.get_email(),
                "fone": obj.get_fone()
            })

        try:
            with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(
                    dados,
                    arquivo,
                    ensure_ascii=False,
                    indent=4
                )
        except OSError as erro:
            print(f"Erro ao salvar os dados: {erro}")


class UI:

    @staticmethod
    def Menu():
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("0 - Sair")
        print("=" * 35)

    @staticmethod
    def Cliente_Listar():
        clientes = ClienteDAO.Listar()

        print("\n--- LISTA DE CLIENTES ---")

        if not clientes:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print("-" * 30)
            print(cliente.ToString())

        print("-" * 30)
        print(f"Total de clientes: {len(clientes)}")

    @staticmethod
    def Cliente_Inserir():
        print("\n--- CADASTRAR CLIENTE ---")

        nome = input("Digite o nome: ").strip()
        email = input("Digite o e-mail: ").strip()
        fone = input("Digite o telefone: ").strip()

        if not nome or not email or not fone:
            print("Erro: todos os campos são obrigatórios.")
            return

        id = ClienteDAO.ProximoId()

        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.Inserir(cliente)

    @staticmethod
    def Cliente_Atualizar():
        print("\n--- ATUALIZAR CLIENTE ---")

        try:
            id = int(input("Digite o ID do cliente: "))
        except ValueError:
            print("Erro: digite um ID numérico.")
            return

        cliente = ClienteDAO.Listar_Id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        print("\nDados atuais:")
        print(cliente.ToString())
        print("\nDigite os novos dados.")
        print("Pressione ENTER para manter o valor atual.")

        nome = input(f"Novo nome [{cliente.get_nome()}]: ").strip()
        email = input(f"Novo e-mail [{cliente.get_email()}]: ").strip()
        fone = input(f"Novo telefone [{cliente.get_fone()}]: ").strip()

        if not nome:
            nome = cliente.get_nome()

        if not email:
            email = cliente.get_email()

        if not fone:
            fone = cliente.get_fone()

        cliente_atualizado = Cliente(id, nome, email, fone)
        ClienteDAO.Atualizar(cliente_atualizado)

    @staticmethod
    def Cliente_Excluir():
        print("\n--- EXCLUIR CLIENTE ---")

        try:
            id = int(input("Digite o ID do cliente: "))
        except ValueError:
            print("Erro: digite um ID numérico.")
            return

        cliente = ClienteDAO.Listar_Id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        print("\nCliente selecionado:")
        print(cliente.ToString())

        confirmacao = input(
            "Tem certeza que deseja excluir? (s/n): "
        ).strip().lower()

        if confirmacao == "s":
            ClienteDAO.Excluir(cliente)
        else:
            print("Exclusão cancelada.")

    @staticmethod
    def Main():

        ClienteDAO.Abrir()

        while True:
            UI.Menu()
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                UI.Cliente_Listar()

            elif opcao == "2":
                UI.Cliente_Inserir()

            elif opcao == "3":
                UI.Cliente_Atualizar()

            elif opcao == "4":
                UI.Cliente_Excluir()

            elif opcao == "0":
                ClienteDAO.Salvar()
                print("Programa encerrado. Até logo!")
                break

            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    UI.Main()