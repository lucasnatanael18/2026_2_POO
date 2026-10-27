from datetime import datetime, date
from enum import Enum

class Turno(Enum):
    Matutino = 1
    Vespertino = 2
    Noturno = 3

class Cargo(Enum):
    Estagiario = 1
    Analista = 2
    Gerente = 3
    Diretor = 4

class Funcionario:
    def __init__(self, nome, matricula, salario, cargo, turno,
                 data_admissao):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario = salario
        self.__cargo = cargo
        self.__turno = turno
        self.__data_admissao = datetime.strptime(
            data_admissao, "%d/%m/%Y"
        ).date()

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    def get_data_admissao(self):
        return self.__data_admissao

    def set_data_admissao(self, data_admissao):
        self.__data_admissao = datetime.strptime(
            data_admissao, "%d/%m/%Y"
        ).date()

    def tempo_trabalho(self):
        hoje = date.today()
        admissao = self.__data_admissao

        anos = hoje.year - admissao.year
        meses = hoje.month - admissao.month
        dias = hoje.day - admissao.day

        if dias < 0:
            meses -= 1

        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"

    def promover(self):
        if self.__cargo == Cargo.Diretor:
            print("O funcionário já possui o maior cargo.")
            return False

        cargos = list(Cargo)
        indice = cargos.index(self.__cargo)

        self.__cargo = cargos[indice + 1]
        self.__salario *= 1.25

        print("Funcionário promovido com sucesso!")
        print("Novo cargo:", self.__cargo.name)
        print(f"Novo salário: R$ {self.__salario:.2f}")

        return True

    def __str__(self):
        return (
            f"Nome: {self.__nome} | "
            f"Matrícula: {self.__matricula} | "
            f"Salário: R$ {self.__salario:.2f} | "
            f"Cargo: {self.__cargo.name} | "
            f"Turno: {self.__turno.name} | "
            f"Admissão: "
            f"{self.__data_admissao.strftime('%d/%m/%Y')} | "
            f"Tempo de trabalho: {self.tempo_trabalho()}"
        )

funcionarios = []

def cadastrar_funcionario():
    print("\n--- Cadastro de Funcionário ---")

    nome = input("Digite o nome do funcionário: ")
    matricula = input("Digite a matrícula: ")

    while True:
        try:
            salario = float(
                input("Digite o salário: R$ ").replace(",", ".")
            )

            if salario < 0:
                print("O salário não pode ser negativo.")
                continue

            break
        except ValueError:
            print("Digite um salário válido.")

    print("\nCargos disponíveis:")
    for cargo in Cargo:
        print(f"{cargo.value} - {cargo.name}")

    while True:
        try:
            opcao_cargo = int(input("Escolha o cargo: "))
            cargo = Cargo(opcao_cargo)
            break
        except ValueError:
            print("Cargo inválido. Digite uma opção da lista.")

    print("\nTurnos disponíveis:")
    for turno in Turno:
        print(f"{turno.value} - {turno.name}")

    while True:
        try:
            opcao_turno = int(input("Escolha o turno: "))
            turno = Turno(opcao_turno)
            break
        except ValueError:
            print("Turno inválido. Digite uma opção da lista.")

    while True:
        texto_data = input(
            "Digite a data de admissão (DD/MM/AAAA): "
        )

        try:
            admissao = datetime.strptime(
                texto_data, "%d/%m/%Y"
            ).date()

            if admissao > date.today():
                print("A data não pode ser futura.")
                continue

            break
        except ValueError:
            print("Data inválida! Use DD/MM/AAAA.")

    funcionario = Funcionario(
        nome, matricula, salario, cargo, turno, texto_data
    )

    funcionarios.append(funcionario)
    print("\nFuncionário cadastrado com sucesso!")

def listar_funcionarios():
    print("\n--- Lista de Funcionários ---")

    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    for funcionario in funcionarios:
        print(funcionario)

def promover_funcionario():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    print("\n--- Promover Funcionário ---")

    for i, funcionario in enumerate(funcionarios, start=1):
        print(
            f"{i} - {funcionario.get_nome()} "
            f"({funcionario.get_cargo().name})"
        )

    try:
        opcao = int(input("Digite o número do funcionário: "))

        if opcao < 1 or opcao > len(funcionarios):
            print("Número inválido.")
            return

        funcionarios[opcao - 1].promover()

    except ValueError:
        print("Digite um número válido.")

while True:
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Promover funcionário")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        listar_funcionarios()
    elif opcao == "3":
        promover_funcionario()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida! Tente novamente.")
