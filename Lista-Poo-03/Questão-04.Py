import math

class Equacao2Grau:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def SetA(self, a):
        self.a = a

    def GetA(self):
        return self.a

    def SetB(self, b):
        self.b = b

    def GetB(self):
        return self.b

    def SetC(self, c):
        self.c = c

    def GetC(self):
        return self.c

    def Delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def TemRaizesReais(self):
        return self.Delta() >= 0

    def Raiz1(self):
        if self.TemRaizesReais():
            return (-self.b + math.sqrt(self.Delta())) / (2 * self.a)
        return None

    def Raiz2(self):
        if self.TemRaizesReais():
            return (-self.b - math.sqrt(self.Delta())) / (2 * self.a)
        return None

    def ToString(self):
        return f"a = {self.a}, b = {self.b}, c = {self.c}"


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

equacao = Equacao2Grau(a, b, c)

print(equacao.ToString())
print("Delta:", equacao.Delta())

if equacao.TemRaizesReais():
    print("Raiz 1:", equacao.Raiz1())
    print("Raiz 2:", equacao.Raiz2())
else:
    print("A equação não possui raízes reais.")
