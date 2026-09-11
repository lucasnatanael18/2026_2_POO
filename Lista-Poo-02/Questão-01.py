import math


class Circulo:
    def __init__(self, raio=0):
        self.raio = raio

    def set_raio(self, raio):
        self.raio = raio

    def get_raio(self):
        return self.raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio

circulo = Circulo()

raio = float(input("Digite o raio do círculo: "))

circulo.set_raio(raio)

print(f"\nRaio: {circulo.get_raio():.2f}")
print(f"Área: {circulo.calcular_area():.2f}")
print(f"Circunferência: {circulo.calcular_circunferencia():.2f}")
