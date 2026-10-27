class Viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        if not isinstance(destino, str) or not destino.strip():
            raise ValueError("O destino deve ser um texto válido.")
        self.__destino = destino

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        if not isinstance(distancia, (int, float)) or isinstance(distancia, bool) or distancia <= 0:
            raise ValueError("A distância deve ser maior que zero.")
        self.__distancia = float(distancia)

    def get_litros(self):
        return self.__litros

    def set_litros(self, litros):
        if not isinstance(litros, (int, float)) or isinstance(litros, bool) or litros <= 0:
            raise ValueError("Os litros devem ser maiores que zero.")
        self.__litros = float(litros)

    def consumo(self):
        return self.__distancia / self.__litros

    def __str__(self):
        return (
            f"Destino: {self.__destino}\n"
            f"Distância: {self.__distancia:.2f} km\n"
            f"Combustível gasto: {self.__litros:.2f} litros"
        )


class ViagemUI:
    @staticmethod
    def menu():
        while True:
            print("\n===== MENU VIAGEM =====")
            print("1 - Calcular")
            print("2 - Fim")

            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao in (1, 2):
                    return opcao
                print("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                print("Digite uma opção numérica válida.")

    @staticmethod
    def main():
        while True:
            opcao = ViagemUI.menu()

            if opcao == 2:
                print("Programa encerrado.")
                break

            ViagemUI.calculo()

    @staticmethod
    def calculo():
        try:
            destino = input("Digite o destino da viagem: ")
            distancia = float(input("Digite a distância percorrida (km): "))
            litros = float(input("Digite a quantidade de combustível (litros): "))

            viagem = Viagem(destino, distancia, litros)

            print("\n--- Dados da viagem ---")
            print(viagem)
            print(f"Consumo médio: {viagem.consumo():.2f} km/l")

        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    ViagemUI.main()
