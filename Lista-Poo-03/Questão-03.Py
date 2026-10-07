class Conversor:
    def __init__(self, num):
        self.num = num

    def SetNum(self, num):
        self.num = num

    def GetNum(self):
        return self.num

    def Binario(self):
        numero = self.num
        binario = ""

        if numero == 0:
            return "0"

        while numero > 0:
            resto = numero % 2
            binario = str(resto) + binario
            numero = numero // 2

        return binario

    def ToString(self):
        return "Decimal: " + str(self.num) + " Binario: " + self.Binario()


numero = int(input("Digite um número decimal: "))

c = Conversor(numero)

print(c.ToString())
