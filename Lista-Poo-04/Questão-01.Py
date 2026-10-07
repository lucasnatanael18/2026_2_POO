class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_artista(self):
        return self.__artista

    def set_artista(self, artista):
        self.__artista = artista

    def get_album(self):
        return self.__album

    def set_album(self, album):
        self.__album = album

    def __str__(self):
        return f"Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album}"


class PlayList:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
        self.__musicas = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def inserir(self, musica):
        self.__musicas.append(musica)

    def listar(self):
        return self.__musicas

    def __str__(self):
        return f"Quantidade de músicas: {len(self.__musicas)}"


class UI:
    def __init__(self):
        self.__playlists = []

    def criar_playlist(self):
        print("\n--- CRIAR PLAYLIST ---")

        nome = input("Digite o nome da playlist: ")
        descricao = input("Digite a descrição da playlist: ")

        playlist = PlayList(nome, descricao)
        self.__playlists.append(playlist)

        print("Playlist criada com sucesso!")

    def listar_playlists(self):
        print("\n--- PLAYLISTS ---")

        if len(self.__playlists) == 0:
            print("Nenhuma playlist cadastrada.")
            return

        for i, playlist in enumerate(self.__playlists):
            print(f"\n{i + 1} - {playlist.get_nome()}")
            print(f"Descrição: {playlist.get_descricao()}")
            print(playlist)

    def inserir_musica(self):
        if len(self.__playlists) == 0:
            print("Nenhuma playlist cadastrada.")
            return

        self.listar_playlists()

        try:
            numero = int(input("\nDigite o número da playlist: "))

            if numero < 1 or numero > len(self.__playlists):
                print("Playlist inválida!")
                return

            print("\n--- INSERIR MÚSICA ---")

            titulo = input("Digite o título da música: ")
            artista = input("Digite o artista: ")
            album = input("Digite o álbum: ")

            musica = Musica(titulo, artista, album)

            self.__playlists[numero - 1].inserir(musica)

            print("Música adicionada com sucesso!")

        except ValueError:
            print("Digite um número válido!")

    def listar_musicas(self):
        if len(self.__playlists) == 0:
            print("Nenhuma playlist cadastrada.")
            return

        self.listar_playlists()

        try:
            numero = int(input("\nDigite o número da playlist: "))

            if numero < 1 or numero > len(self.__playlists):
                print("Playlist inválida!")
                return

            playlist = self.__playlists[numero - 1]

            print(f"\n--- MÚSICAS DA PLAYLIST '{playlist.get_nome()}' ---")

            musicas = playlist.listar()

            if len(musicas) == 0:
                print("Essa playlist não possui músicas.")
                return

            for i, musica in enumerate(musicas):
                print(f"{i + 1} - {musica}")

        except ValueError:
            print("Digite um número válido!")

    def executar(self):
        while True:
            print("\n==============================")
            print("        MENU PRINCIPAL")
            print("==============================")
            print("1 - Criar playlist")
            print("2 - Listar playlists")
            print("3 - Inserir música")
            print("4 - Listar músicas")
            print("0 - Sair")

            opcao = input("\nDigite uma opção: ")

            if opcao == "1":
                self.criar_playlist()

            elif opcao == "2":
                self.listar_playlists()

            elif opcao == "3":
                self.inserir_musica()

            elif opcao == "4":
                self.listar_musicas()

            elif opcao == "0":
                print("Programa encerrado!")
                break

            else:
                print("Opção inválida!")


ui = UI()
ui.executar()
