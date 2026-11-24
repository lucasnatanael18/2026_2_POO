class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria

    def __str__(self):
        return (
            f"ID: {self.id} | Descrição: {self.descricao} | "
            f"Preço: R$ {self.preco:.2f} | Estoque: {self.estoque} | "
            f"ID da categoria: {self.id_categoria}"
        )
