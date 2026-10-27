from datetime import datetime, timedelta

class PlayList:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao

    def TempoTotal(self, itens, musicas):
        total = timedelta()

        for item in itens:
            if item.id_playlist == self.id:
                musica = next(
                    (m for m in musicas if m.id == item.id_musica),
                    None
                )

                if musica is not None:
                    total += musica.duracao

        return total

    def ToString(self):
        return (
            f"ID: {self.id} | "
            f"Nome: {self.nome} | "
            f"Descrição: {self.descricao}"
        )

    def __str__(self):
        return self.ToString()

class Musica:
    def __init__(self, id, titulo, artista, album, duracao):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

    def setArtista(self, artista):
        self.artista = artista

    def getArtista(self):
        return self.artista

    def setAlbum(self, album):
        self.album = album

    def getAlbum(self):
        return self.album

    def setDuracao(self, duracao):
        self.duracao = duracao

    def getDuracao(self):
        return self.duracao

    def ToString(self):
        return (
            f"ID: {self.id} | "
            f"Título: {self.titulo} | "
            f"Artista: {self.artista} | "
            f"Álbum: {self.album} | "
            f"Duração: {self.duracao}"
        )

    def __str__(self):
        return self.ToString()

class PlayListItem:
    def __init__(self, id, id_playlist, id_musica,
                 data_inclusao, sequencia):
        self.id = id
        self.id_playlist = id_playlist
        self.id_musica = id_musica
        self.data_inclusao = data_inclusao
        self.sequencia = sequencia

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setIdPlaylist(self, id_playlist):
        self.id_playlist = id_playlist

    def getIdPlaylist(self):
        return self.id_playlist

    def setIdMusica(self, id_musica):
        self.id_musica = id_musica

    def getIdMusica(self):
        return self.id_musica

    def setDataInclusao(self, data_inclusao):
        self.data_inclusao = data_inclusao

    def getDataInclusao(self):
        return self.data_inclusao

    def setSequencia(self, sequencia):
        self.sequencia = sequencia

    def getSequencia(self):
        return self.sequencia

    def ToString(self):
        return (
            f"ID do item: {self.id} | "
            f"ID da playlist: {self.id_playlist} | "
            f"ID da música: {self.id_musica} | "
            f"Inclusão: {self.data_inclusao.strftime('%d/%m/%Y %H:%M:%S')} | "
            f"Sequência: {self.sequencia}"
        )

    def __str__(self):
        return self.ToString()

class UI:
    def __init__(self):
        self.playlists = []
        self.musicas = []
        self.itens = []

    def BuscarPlaylist(self, id):
        return next(
            (p for p in self.playlists if p.id == id),
            None
        )

    def BuscarMusica(self, id):
        return next(
            (m for m in self.musicas if m.id == id),
            None
        )

    def BuscarItem(self, id):
        return next(
            (i for i in self.itens if i.id == id),
            None
        )

    def Menu(self):
        print("\n========== PLAYLIST ==========")
        print("1  - Inserir playlist")
        print("2  - Listar playlists")
        print("3  - Atualizar playlist")
        print("4  - Excluir playlist")
        print("5  - Mostrar tempo total da playlist")
        print("6  - Inserir música")
        print("7  - Listar músicas")
        print("8  - Atualizar música")
        print("9  - Excluir música")
        print("10 - Inserir música em uma playlist")
        print("11 - Listar músicas de uma playlist")
        print("12 - Atualizar item de playlist")
        print("13 - Excluir música de uma playlist")
        print("0  - Sair")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def Main(self):
        while True:
            opcao = self.Menu()

            try:
                if opcao == 0:
                    print("Programa encerrado.")
                    break
                elif opcao == 1:
                    self.InserirPlaylist()
                elif opcao == 2:
                    self.ListarPlaylists()
                elif opcao == 3:
                    self.AtualizarPlaylist()
                elif opcao == 4:
                    self.ExcluirPlaylist()
                elif opcao == 5:
                    self.MostrarTempoTotal()
                elif opcao == 6:
                    self.InserirMusica()
                elif opcao == 7:
                    self.ListarMusicas()
                elif opcao == 8:
                    self.AtualizarMusica()
                elif opcao == 9:
                    self.ExcluirMusica()
                elif opcao == 10:
                    self.InserirItem()
                elif opcao == 11:
                    self.ListarItensPlaylist()
                elif opcao == 12:
                    self.AtualizarItem()
                elif opcao == 13:
                    self.ExcluirItem()
                else:
                    print("Opção inválida.")

            except ValueError:
                print("Valor inválido. Tente novamente.")

    def InserirPlaylist(self):
        id = int(input("ID da playlist: "))

        if self.BuscarPlaylist(id):
            print("Já existe uma playlist com esse ID.")
            return

        nome = input("Nome da playlist: ")
        descricao = input("Descrição: ")

        self.playlists.append(PlayList(id, nome, descricao))
        print("Playlist cadastrada com sucesso!")

    def ListarPlaylists(self):
        if not self.playlists:
            print("Nenhuma playlist cadastrada.")
            return

        for playlist in self.playlists:
            print(playlist.ToString())

    def AtualizarPlaylist(self):
        id = int(input("ID da playlist: "))
        playlist = self.BuscarPlaylist(id)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        playlist.setNome(input("Novo nome: "))
        playlist.setDescricao(input("Nova descrição: "))
        print("Playlist atualizada com sucesso!")

    def ExcluirPlaylist(self):
        id = int(input("ID da playlist: "))
        playlist = self.BuscarPlaylist(id)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        self.itens = [
            item for item in self.itens
            if item.id_playlist != id
        ]

        self.playlists.remove(playlist)
        print("Playlist excluída com sucesso!")

    def MostrarTempoTotal(self):
        id = int(input("ID da playlist: "))
        playlist = self.BuscarPlaylist(id)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        total = playlist.TempoTotal(self.itens, self.musicas)
        print(f"Tempo total de '{playlist.nome}': {total}")

    def InserirMusica(self):
        id = int(input("ID da música: "))

        if self.BuscarMusica(id):
            print("Já existe uma música com esse ID.")
            return

        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        horas = int(input("Duração - horas: "))
        minutos = int(input("Duração - minutos: "))
        segundos = int(input("Duração - segundos: "))

        if horas < 0 or minutos < 0 or segundos < 0:
            print("A duração não pode ser negativa.")
            return

        duracao = timedelta(
            hours=horas,
            minutes=minutos,
            seconds=segundos
        )

        musica = Musica(id, titulo, artista, album, duracao)
        self.musicas.append(musica)
        print("Música cadastrada com sucesso!")

    def ListarMusicas(self):
        if not self.musicas:
            print("Nenhuma música cadastrada.")
            return

        for musica in self.musicas:
            print(musica.ToString())

    def AtualizarMusica(self):
        id = int(input("ID da música: "))
        musica = self.BuscarMusica(id)

        if musica is None:
            print("Música não encontrada.")
            return

        musica.setTitulo(input("Novo título: "))
        musica.setArtista(input("Novo artista: "))
        musica.setAlbum(input("Novo álbum: "))

        horas = int(input("Nova duração - horas: "))
        minutos = int(input("Nova duração - minutos: "))
        segundos = int(input("Nova duração - segundos: "))

        if horas < 0 or minutos < 0 or segundos < 0:
            print("A duração não pode ser negativa.")
            return

        musica.setDuracao(
            timedelta(
                hours=horas,
                minutes=minutos,
                seconds=segundos
            )
        )

        print("Música atualizada com sucesso!")

    def ExcluirMusica(self):
        id = int(input("ID da música: "))
        musica = self.BuscarMusica(id)

        if musica is None:
            print("Música não encontrada.")
            return

        if any(item.id_musica == id for item in self.itens):
            print("A música está em uma playlist. Remova os itens associados primeiro.")
            return

        self.musicas.remove(musica)
        print("Música excluída com sucesso!")

    def InserirItem(self):
        id = int(input("ID do novo item: "))

        if self.BuscarItem(id):
            print("Já existe um item com esse ID.")
            return

        id_playlist = int(input("ID da playlist: "))
        playlist = self.BuscarPlaylist(id_playlist)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        id_musica = int(input("ID da música: "))
        musica = self.BuscarMusica(id_musica)

        if musica is None:
            print("Música não encontrada.")
            return

        sequencia = int(input("Posição da música na playlist: "))

        if sequencia < 1:
            print("A sequência deve ser maior ou igual a 1.")
            return

        if any(
            item.id_playlist == id_playlist
            and item.sequencia == sequencia
            for item in self.itens
        ):
            print("Já existe uma música nessa posição da playlist.")
            return

        item = PlayListItem(
            id,
            id_playlist,
            id_musica,
            datetime.now(),
            sequencia
        )

        self.itens.append(item)
        print("Música adicionada à playlist com sucesso!")

    def ListarItensPlaylist(self):
        id_playlist = int(input("ID da playlist: "))
        playlist = self.BuscarPlaylist(id_playlist)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        itens = sorted(
            [
                item for item in self.itens
                if item.id_playlist == id_playlist
            ],
            key=lambda item: item.sequencia
        )

        if not itens:
            print("Essa playlist não possui músicas.")
            return

        print(f"\nPlaylist: {playlist.nome}")

        for item in itens:
            musica = self.BuscarMusica(item.id_musica)

            if musica:
                print(
                    f"Posição {item.sequencia}: "
                    f"{musica.ToString()}"
                )
                print(f"   {item.ToString()}")

    def AtualizarItem(self):
        id = int(input("ID do item que deseja atualizar: "))
        item = self.BuscarItem(id)

        if item is None:
            print("Item não encontrado.")
            return

        id_playlist = int(input("Novo ID da playlist: "))
        playlist = self.BuscarPlaylist(id_playlist)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        id_musica = int(input("Novo ID da música: "))

        if self.BuscarMusica(id_musica) is None:
            print("Música não encontrada.")
            return

        sequencia = int(input("Nova posição na playlist: "))

        if sequencia < 1:
            print("A sequência deve ser maior ou igual a 1.")
            return

        conflito = any(
            outro.id != id
            and outro.id_playlist == id_playlist
            and outro.sequencia == sequencia
            for outro in self.itens
        )

        if conflito:
            print("Já existe uma música nessa posição da playlist.")
            return

        item.setIdPlaylist(id_playlist)
        item.setIdMusica(id_musica)
        item.setSequencia(sequencia)
        item.setDataInclusao(datetime.now())

        print("Item atualizado com sucesso!")

    def ExcluirItem(self):
        id = int(input("ID do item que deseja excluir: "))
        item = self.BuscarItem(id)

        if item is None:
            print("Item não encontrado.")
            return

        self.itens.remove(item)
        print("Música removida da playlist com sucesso!")

if __name__ == "__main__":
    app = UI()
    app.Main()
