from datetime import datetime, date
from enum import Enum

class SituacaoEstagio(Enum):
    Cadastrado = 1
    Iniciado = 2
    Cancelado = 3
    Finalizado = 4

class Estagio:
    def __init__(self, estagiario, empresa):
        self.__estagiario = estagiario
        self.__empresa = empresa
        self.__data_inicio = None
        self.__data_cancelamento = None
        self.__data_fim = None
        self.__situacao = SituacaoEstagio.Cadastrado

    def get_estagiario(self):
        return self.__estagiario

    def set_estagiario(self, estagiario):
        self.__estagiario = estagiario

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_data_inicio(self):
        return self.__data_inicio

    def get_data_cancelamento(self):
        return self.__data_cancelamento

    def get_data_fim(self):
        return self.__data_fim

    def iniciar(self, data):
        if self.__situacao != SituacaoEstagio.Cadastrado:
            return False

        if data.date() > datetime.now().date():
            return False

        self.__data_inicio = data
        self.__situacao = SituacaoEstagio.Iniciado
        return True

    def cancelar(self, data):
        if self.__situacao not in (
            SituacaoEstagio.Cadastrado,
            SituacaoEstagio.Iniciado
        ):
            return False

        if data.date() > datetime.now().date():
            return False

        if (self.__data_inicio is not None
                and data < self.__data_inicio):
            return False

        self.__data_cancelamento = data
        self.__situacao = SituacaoEstagio.Cancelado
        return True

    def finalizar(self, data):
        if self.__situacao != SituacaoEstagio.Iniciado:
            return False

        if data.date() > datetime.now().date():
            return False

        if data < self.__data_inicio:
            return False

        self.__data_fim = data
        self.__situacao = SituacaoEstagio.Finalizado
        return True

    def tempo_estagio(self):
        if self.__data_inicio is None:
            return "Estágio ainda não iniciado."

        if self.__situacao == SituacaoEstagio.Cancelado:
            data_final = self.__data_cancelamento
        elif self.__situacao == SituacaoEstagio.Finalizado:
            data_final = self.__data_fim
        else:
            data_final = datetime.now()

        tempo = data_final - self.__data_inicio

        dias = tempo.days
        horas = tempo.seconds // 3600

        return f"{dias} dias e {horas} horas"

    def situacao(self):
        return self.__situacao

    def __str__(self):
        inicio = (
            self.__data_inicio.strftime("%d/%m/%Y")
            if self.__data_inicio else "Não iniciado"
        )

        cancelamento = (
            self.__data_cancelamento.strftime("%d/%m/%Y")
            if self.__data_cancelamento else "Não cancelado"
        )

        fim = (
            self.__data_fim.strftime("%d/%m/%Y")
            if self.__data_fim else "Não finalizado"
        )

        return (
            f"Estagiário: {self.__estagiario} | "
            f"Empresa: {self.__empresa} | "
            f"Início: {inicio} | "
            f"Cancelamento: {cancelamento} | "
            f"Fim: {fim} | "
            f"Situação: {self.__situacao.name} | "
            f"Tempo: {self.tempo_estagio()}"
        )

estagios = []

def ler_data(mensagem):
    while True:
        texto = input(mensagem)

        try:
            data = datetime.strptime(texto, "%d/%m/%Y")

            if data.date() > date.today():
                print("A data não pode ser futura.")
                continue

            return data

        except ValueError:
            print("Data inválida! Use DD/MM/AAAA.")

def cadastrar_estagio():
    print("\n--- Cadastro de Estágio ---")

    estagiario = input("Digite o nome do estagiário: ")
    empresa = input("Digite o nome da empresa: ")

    estagio = Estagio(estagiario, empresa)
    estagios.append(estagio)

    print("Estágio cadastrado com sucesso!")


def listar_empresa():
    print("\n--- Estágios por Empresa ---")

    if not estagios:
        print("Nenhum estágio cadastrado.")
        return

    for estagio in sorted(
        estagios, key=lambda e: e.get_empresa().lower()
    ):
        print(estagio)


def listar_estagiario():
    print("\n--- Estágios por Estagiário ---")

    if not estagios:
        print("Nenhum estágio cadastrado.")
        return

    for estagio in sorted(
        estagios, key=lambda e: e.get_estagiario().lower()
    ):
        print(estagio)


def listar_situacao():
    print("\n--- Listar por Situação ---")

    for situacao in SituacaoEstagio:
        print(f"{situacao.value} - {situacao.name}")

    try:
        opcao = int(input("Digite o número da situação desejada: "))
        situacao_escolhida = SituacaoEstagio(opcao)
    except (ValueError, TypeError):
        print("Situação inválida.")
        return

    encontrados = [
        e for e in estagios
        if e.situacao() == situacao_escolhida
    ]

    if not encontrados:
        print("Nenhum estágio encontrado nessa situação.")
        return

    for estagio in encontrados:
        print(estagio)


def alterar_situacao():
    if not estagios:
        print("Nenhum estágio cadastrado.")
        return

    print("\n--- Alterar Situação do Estágio ---")

    for i, estagio in enumerate(estagios, start=1):
        print(f"{i} - {estagio}")

    try:
        numero = int(input("Digite o número do estágio: "))

        if numero < 1 or numero > len(estagios):
            print("Número inválido.")
            return

        estagio = estagios[numero - 1]

    except ValueError:
        print("Digite um número válido.")
        return

    print("\n1 - Iniciar estágio")
    print("2 - Cancelar estágio")
    print("3 - Finalizar estágio")

    opcao = input("Escolha uma operação: ")

    if opcao == "1":
        data = ler_data("Digite a data de início (DD/MM/AAAA): ")
        sucesso = estagio.iniciar(data)

    elif opcao == "2":
        data = ler_data(
            "Digite a data de cancelamento (DD/MM/AAAA): "
        )
        sucesso = estagio.cancelar(data)

    elif opcao == "3":
        data = ler_data(
            "Digite a data de finalização (DD/MM/AAAA): "
        )
        sucesso = estagio.finalizar(data)

    else:
        print("Opção inválida.")
        return

    if sucesso:
        print("Operação realizada com sucesso!")
    else:
        print("Não foi possível realizar a operação.")
        print("Verifique a situação atual e as datas informadas.")

while True:
    print("1 - Cadastrar estágio")
    print("2 - Listar estágios por empresa")
    print("3 - Listar estágios por estagiário")
    print("4 - Listar estágios por situação")
    print("5 - Iniciar, cancelar ou finalizar estágio")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_estagio()
    elif opcao == "2":
        listar_empresa()
    elif opcao == "3":
        listar_estagiario()
    elif opcao == "4":
        listar_situacao()
    elif opcao == "5":
        alterar_situacao()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida! Tente novamente.")
