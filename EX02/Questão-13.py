def RemoverEspacos(texto):
    return " ".join(texto.split())


texto = input("Digite um texto: ")

print(RemoverEspacos(texto))