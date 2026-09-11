class Viagem:
    def __init__(self, distancia, tempo):
        self.__distancia = distancia
        self.__tempo = tempo

    def calcular_velocidade_media(self):
        return self.__distancia / self.__tempo

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, tempo):
        self.__tempo = tempo


distancia = float(input("Digite a distância da viagem em km: "))
tempo = float(input("Digite o tempo gasto em horas: "))

viagem = Viagem(distancia, tempo)

print(f"Distância: {viagem.get_distancia()} km")
print(f"Tempo: {viagem.get_tempo()} horas")
print(f"Velocidade média: {viagem.calcular_velocidade_media():.2f} km/h")