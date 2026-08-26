frase = input("Digite uma frase: ")

palavras = frase.split()

for i in range(len(palavras)):
    print(" ".join(palavras[i:]))