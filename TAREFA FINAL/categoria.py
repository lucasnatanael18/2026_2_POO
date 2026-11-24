class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return f"ID: {self.id} | Descrição: {self.descricao}"
