class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print("Saque realizado com sucesso!")

if __name__ == "__main__":
    titular = input("Digite o nome do titular: ")
    numero = input("Digite o número da conta: ")
    saldo = float(input("Digite o saldo inicial: "))
    
    conta = ContaBancaria(titular, numero, saldo)
    
    print("\n--- Dados da conta ---")
    print("Titular:", conta.get_titular())
    print("Número:", conta.get_numero())
    print("Saldo: R$", conta.get_saldo())
    
    valor_dep = float(input("\nDigite o valor para depósito: "))
    conta.depositar(valor_dep)
    
    print("Saldo atual: R$", conta.get_saldo())
    
    valor_saque = float(input("\nDigite o valor para saque: "))
    conta.sacar(valor_saque)
    
    print("Saldo atual: R$", conta.get_saldo())