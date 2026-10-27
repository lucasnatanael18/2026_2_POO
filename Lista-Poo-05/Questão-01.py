from datetime import datetime, date

class Paciente:
    def __init__(self, nome, cpf, telefone, data_nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__data_nascimento = datetime.strptime(
            data_nascimento, "%d/%m/%Y"
        ).date()

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_data_nascimento(self):
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = datetime.strptime(
            data_nascimento, "%d/%m/%Y"
        ).date()

    def idade(self):
        hoje = date.today()
        nascimento = self.__data_nascimento

        anos = hoje.year - nascimento.year
        meses = hoje.month - nascimento.month

        if hoje.day < nascimento.day:
            meses -= 1

        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"

    def __str__(self):
        return (
            f"Nome: {self.__nome} | "
            f"CPF: {self.__cpf} | "
            f"Telefone: {self.__telefone} | "
            f"Data de nascimento: "
            f"{self.__data_nascimento.strftime('%d/%m/%Y')} | "
            f"Idade: {self.idade()}"
        )

pacientes = []


def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")

    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone: ")

    while True:
        data_nascimento = input(
            "Digite a data de nascimento (DD/MM/AAAA): "
        )

        try:
            nascimento = datetime.strptime(
                data_nascimento, "%d/%m/%Y"
            ).date()

            if nascimento > date.today():
                print("A data não pode ser no futuro.")
                continue

            break
        except ValueError:
            print("Data inválida! Digite novamente.")

    paciente = Paciente(nome, cpf, telefone, data_nascimento)
    pacientes.append(paciente)

    print("\nPaciente cadastrado com sucesso!")


def listar_alfabetica():
    print("\n--- Pacientes por ordem alfabética ---")

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    for paciente in sorted(
        pacientes, key=lambda p: p.get_nome().lower()
    ):
        print(paciente)


def listar_por_idade():
    print("\n--- Pacientes por ordem de idade ---")

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    for paciente in sorted(
        pacientes, key=lambda p: p.get_data_nascimento()
    ):
        print(paciente)

while True:
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes por ordem alfabética")
    print("3 - Listar pacientes por ordem de idade")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        listar_alfabetica()
    elif opcao == "3":
        listar_por_idade()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida! Tente novamente.")
