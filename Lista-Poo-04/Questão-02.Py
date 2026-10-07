class Cliente:
    def __init__(self, nome, cpf, limite):
        self.nome = nome
        self.cpf = cpf
        self.limite = limite
        self.socio = None

    def SetSocio(self, cliente):
        self.socio = cliente

        if cliente.socio != self:
            cliente.socio = self

    def GetLimite(self):
        if self.socio is not None:
            return self.limite + self.socio.limite

        return self.limite

    def ToString(self):
        texto = f"Nome: {self.nome}\n"
        texto += f"CPF: {self.cpf}\n"
        texto += f"Limite: R$ {self.limite:.2f}\n"
        texto += f"Limite total: R$ {self.GetLimite():.2f}\n"

        if self.socio is not None:
            texto += f"Sócio: {self.socio.nome}\n"
        else:
            texto += "Sócio: Nenhum\n"

        return texto


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def GetNome(self):
        return self.nome

    def SetNome(self, nome):
        self.nome = nome

    def Inserir(self, cliente):
        self.clientes.append(cliente)

    def Listar(self):
        return self.clientes

    def ToString(self):
        texto = f"Empresa: {self.nome}\n"
        texto += f"Quantidade de clientes: {len(self.clientes)}\n"

        return texto

class UI:
    def __init__(self):
        self.empresas = []

    def cadastrar_empresa(self):
        print("\n===== CADASTRAR EMPRESA =====")

        nome = input("Digite o nome da empresa: ")

        empresa = Empresa(nome)
        self.empresas.append(empresa)

        print("Empresa cadastrada com sucesso!")

    def listar_empresas(self):
        print("\n===== EMPRESAS CADASTRADAS =====")

        if len(self.empresas) == 0:
            print("Nenhuma empresa cadastrada.")
            return

        for i, empresa in enumerate(self.empresas):
            print(f"{i + 1} - {empresa.nome}")

    def cadastrar_cliente(self):
        if len(self.empresas) == 0:
            print("\nNenhuma empresa cadastrada.")
            return

        self.listar_empresas()

        try:
            numero = int(input("\nEscolha a empresa: "))

            if numero < 1 or numero > len(self.empresas):
                print("Empresa inválida.")
                return

            empresa = self.empresas[numero - 1]

            print(f"\n===== CADASTRAR CLIENTE EM {empresa.nome} =====")

            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")

            while True:
                try:
                    limite = float(input("Digite o limite de crédito: R$ "))

                    if limite < 0:
                        print("O limite não pode ser negativo.")
                    else:
                        break

                except ValueError:
                    print("Digite um valor válido.")

            cliente = Cliente(nome, cpf, limite)

            empresa.Inserir(cliente)

            print("\nCliente cadastrado com sucesso!")

        except ValueError:
            print("Digite um número válido.")

    def listar_clientes(self):
        if len(self.empresas) == 0:
            print("\nNenhuma empresa cadastrada.")
            return

        self.listar_empresas()

        try:
            numero = int(input("\nEscolha a empresa: "))

            if numero < 1 or numero > len(self.empresas):
                print("Empresa inválida.")
                return

            empresa = self.empresas[numero - 1]

            print(f"\n===== CLIENTES DA EMPRESA {empresa.nome} =====")

            clientes = empresa.Listar()

            if len(clientes) == 0:
                print("Nenhum cliente cadastrado.")
                return

            for i, cliente in enumerate(clientes):
                print(f"\n--- Cliente {i + 1} ---")
                print(cliente.ToString())

        except ValueError:
            print("Digite um número válido.")

    def associar_socios(self):
        if len(self.empresas) == 0:
            print("\nNenhuma empresa cadastrada.")
            return

        self.listar_empresas()

        try:
            numero = int(input("\nEscolha a empresa: "))

            if numero < 1 or numero > len(self.empresas):
                print("Empresa inválida.")
                return

            empresa = self.empresas[numero - 1]
            clientes = empresa.Listar()

            if len(clientes) < 2:
                print("É necessário ter pelo menos 2 clientes.")
                return

            print(f"\n===== CLIENTES DE {empresa.nome} =====")

            for i, cliente in enumerate(clientes):
                print(f"{i + 1} - {cliente.nome} - CPF: {cliente.cpf}")

            cliente1_numero = int(
                input("\nDigite o número do primeiro cliente: ")
            )

            cliente2_numero = int(
                input("Digite o número do segundo cliente: ")
            )

            if cliente1_numero < 1 or cliente1_numero > len(clientes):
                print("Primeiro cliente inválido.")
                return

            if cliente2_numero < 1 or cliente2_numero > len(clientes):
                print("Segundo cliente inválido.")
                return

            if cliente1_numero == cliente2_numero:
                print("Um cliente não pode ser sócio dele mesmo.")
                return

            cliente1 = clientes[cliente1_numero - 1]
            cliente2 = clientes[cliente2_numero - 1]

            cliente1.SetSocio(cliente2)

            print("\nSociedade realizada com sucesso!")
            print(f"{cliente1.nome} é sócio de {cliente2.nome}.")

        except ValueError:
            print("Digite números válidos.")

    def executar(self):

        while True:

            print("\n================================")
            print("       SISTEMA DA EMPRESA")
            print("================================")
            print("1 - Cadastrar empresa")
            print("2 - Listar empresas")
            print("3 - Cadastrar cliente")
            print("4 - Listar clientes")
            print("5 - Associar sócios")
            print("0 - Sair")
            print("================================")

            opcao = input("Digite uma opção: ")

            if opcao == "1":
                self.cadastrar_empresa()

            elif opcao == "2":
                self.listar_empresas()

            elif opcao == "3":
                self.cadastrar_cliente()

            elif opcao == "4":
                self.listar_clientes()

            elif opcao == "5":
                self.associar_socios()

            elif opcao == "0":
                print("\nPrograma encerrado.")
                break

            else:
                print("\nOpção inválida!")


ui = UI()
ui.executar()
