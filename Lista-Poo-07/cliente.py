class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | E-mail: {self.email} | Fone: {self.fone}"
