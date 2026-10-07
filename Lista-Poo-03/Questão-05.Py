from datetime import datetime

class Data:
    def __init__(self, dia, mes, ano):
        self.SetDia(dia)
        self.SetMes(mes)
        self.SetAno(ano)

        self._validar()

    def _validar(self):
        try:
            datetime(self.ano, self.mes, self.dia)
        except ValueError:
            raise ValueError("Data inválida!")

    def SetDia(self, dia):
        self.dia = dia

    def GetDia(self):
        return self.dia

    def SetMes(self, mes):
        self.mes = mes

    def GetMes(self):
        return self.mes

    def SetAno(self, ano):
        self.ano = ano

    def GetAno(self):
        return self.ano

    def SetData(self, data):
        try:
            data_convertida = datetime.strptime(data, "%d/%m/%Y")

            self.dia = data_convertida.day
            self.mes = data_convertida.month
            self.ano = data_convertida.year

        except ValueError:
            raise ValueError("Data inválida!")

    def ToString(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"


# Programa principal
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

try:
    data = Data(dia, mes, ano)

    print("Data:", data.ToString())

    nova_data = input("Digite uma nova data (dd/mm/aaaa): ")
    data.SetData(nova_data)

    print("Nova data:", data.ToString())

except ValueError:
    print("Data inválida!")
