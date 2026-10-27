from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, dt, ds, t):
        self.id = id
        self.data = dt
        self.distancia = ds
        self.tempo = t

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setDistancia(self, distancia):
        self.distancia = distancia

    def getDistancia(self):
        return self.distancia

    def setTempo(self, tempo):
        self.tempo = tempo

    def getTempo(self):
        return self.tempo

    def Pace(self):
        if self.distancia <= 0:
            return None

        minutos = self.tempo.total_seconds() / 60
        return minutos / self.distancia

    def ToString(self):
        pace = self.Pace()

        if pace is None:
            pace_texto = "Indefinido"
        else:
            minutos = int(pace)
            segundos = round((pace - minutos) * 60)
            if segundos == 60:
                minutos += 1
                segundos = 0
            pace_texto = f"{minutos}:{segundos:02d} min/km"

        return (
            f"ID: {self.id} | "
            f"Data: {self.data.strftime('%d/%m/%Y %H:%M')} | "
            f"Distância: {self.distancia:.2f} km | "
            f"Tempo: {self.tempo} | "
            f"Pace: {pace_texto}"
        )

    def __str__(self):
        return self.ToString()


class TreinoUI:
    def __init__(self):
        self.treinos = []

    def Main(self):
        opcao = 0

        while opcao != 8:
            opcao = self.Menu()

            if opcao == 1:
                self.Inserir()
            elif opcao == 2:
                self.Listar()
            elif opcao == 3:
                self.Listar_Id()
            elif opcao == 4:
                self.Atualizar()
            elif opcao == 5:
                self.Excluir()
            elif opcao == 6:
                self.MaisRapido()
            elif opcao == 8:
                print("Programa encerrado.")
            else:
                print("Opção inválida.")

    def Menu(self):
        print("\n===== MENU DE TREINOS =====")
        print("1 - Inserir treino")
        print("2 - Listar todos os treinos")
        print("3 - Listar treino por ID")
        print("4 - Atualizar treino")
        print("5 - Excluir treino")
        print("6 - Mostrar treino mais rápido")
        print("8 - Sair")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    def BuscarPorId(self, id):
        for treino in self.treinos:
            if treino.id == id:
                return treino
        return None

    def Inserir(self):
        try:
            id = int(input("ID do treino: "))

            if self.BuscarPorId(id) is not None:
                print("Já existe um treino com esse ID.")
                return

            data_texto = input("Data e hora (dd/mm/aaaa HH:MM): ")
            data = datetime.strptime(data_texto, "%d/%m/%Y %H:%M")

            distancia = float(input("Distância percorrida (km): "))

            if distancia <= 0:
                print("A distância deve ser maior que zero.")
                return

            horas = int(input("Horas do treino: "))
            minutos = int(input("Minutos do treino: "))
            segundos = int(input("Segundos do treino: "))

            if horas < 0 or minutos < 0 or segundos < 0:
                print("O tempo não pode ser negativo.")
                return

            tempo = timedelta(
                hours=horas,
                minutes=minutos,
                seconds=segundos
            )

            treino = Treino(id, data, distancia, tempo)
            self.treinos.append(treino)

            print("Treino cadastrado com sucesso!")

        except ValueError:
            print("Dados inválidos. Verifique os valores informados.")

    def Listar(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
            return

        print("\n===== TODOS OS TREINOS =====")
        for treino in self.treinos:
            print(treino.ToString())

    def Listar_Id(self):
        try:
            id = int(input("Informe o ID do treino: "))
            treino = self.BuscarPorId(id)

            if treino is None:
                print("Treino não encontrado.")
            else:
                print(treino.ToString())

        except ValueError:
            print("ID inválido.")

    def Atualizar(self):
        try:
            id = int(input("ID do treino que deseja atualizar: "))
            treino = self.BuscarPorId(id)

            if treino is None:
                print("Treino não encontrado.")
                return

            print("Informe os novos dados:")

            data_texto = input("Nova data e hora (dd/mm/aaaa HH:MM): ")
            data = datetime.strptime(data_texto, "%d/%m/%Y %H:%M")

            distancia = float(input("Nova distância (km): "))

            if distancia <= 0:
                print("A distância deve ser maior que zero.")
                return

            horas = int(input("Horas do treino: "))
            minutos = int(input("Minutos do treino: "))
            segundos = int(input("Segundos do treino: "))

            if horas < 0 or minutos < 0 or segundos < 0:
                print("O tempo não pode ser negativo.")
                return

            tempo = timedelta(
                hours=horas,
                minutes=minutos,
                seconds=segundos
            )

            treino.setData(data)
            treino.setDistancia(distancia)
            treino.setTempo(tempo)

            print("Treino atualizado com sucesso!")

        except ValueError:
            print("Dados inválidos. Verifique os valores informados.")

    def Excluir(self):
        try:
            id = int(input("ID do treino que deseja excluir: "))
            treino = self.BuscarPorId(id)

            if treino is None:
                print("Treino não encontrado.")
                return

            self.treinos.remove(treino)
            print("Treino excluído com sucesso!")

        except ValueError:
            print("ID inválido.")

    def MaisRapido(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
            return

        validos = [
            treino for treino in self.treinos
            if treino.distancia > 0 and treino.tempo.total_seconds() > 0
        ]

        if not validos:
            print("Não existem treinos com tempo e distância válidos.")
            return

        mais_rapido = min(validos, key=lambda treino: treino.Pace())

        print("\n===== TREINO MAIS RÁPIDO =====")
        print(mais_rapido.ToString())


if __name__ == "__main__":
    app = TreinoUI()
    app.Main()
