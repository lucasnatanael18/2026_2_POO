class EntradaCinema:
    def __init__(self, dia, horario):
        self.__dia = dia
        self.__horario = horario

    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = dia

    def get_horario(self):
        return self.__horario

    def set_horario(self, horario):
        self.__horario = horario

    def calcular_inteira(self):
        dia = self.__dia.lower()

        if dia == "quarta":
            return 8.00

        if dia in ["segunda", "terça", "quinta"]:
            valor = 16.00

        elif dia in ["sexta", "sábado", "domingo"]:
            valor = 20.00

        else:
            return 0.00

        if self.__horario >= 17:
            valor = valor * 1.5

        return valor

    def calcular_meia(self):
        dia = self.__dia.lower()

        if dia == "quarta":
            return 8.00

        return self.calcular_inteira() / 2

if __name__ == "__main__":
    dia = input("Digite o dia da sessão: ")
    horario = float(input("Digite o horário da sessão (ex: 18.5 para 18h30): "))
    
    entrada = EntradaCinema(dia, horario)
    
    print("\n--- Dados da sessão ---")
    print("Dia:", entrada.get_dia())
    print("Horário:", entrada.get_horario())
    
    print(f"Valor da entrada inteira: R$ {entrada.calcular_inteira():.2f}")
    print(f"Valor da meia-entrada: R$ {entrada.calcular_meia():.2f}")
