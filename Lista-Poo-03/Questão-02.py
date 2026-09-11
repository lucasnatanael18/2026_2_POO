class Frete:
    def __init__(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso
        
    def CalcFrete(self):
        return self.distancia * self.peso * 0.01
        
    def ToString(self):
        return "Distancia: " + str(self.distancia) + " Km | Peso: " + str(self.peso) + " Kg"

# Programa principal
print("===== CALCULO DE FRETE =====")
distancia = float(input("Digite a distancia em Km: "))
peso = float(input("Digite o peso em Kg: "))

frete = Frete(distancia, peso)

print()
print("===== RESULTADO =====")
print(frete.ToString())
print("Valor do frete: R$ {:.2f}".format(frete.CalcFrete()))