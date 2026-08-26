frase = input("Digite uma frase: ")

palavras = frase.split()

for palavra in palavras:
    print(palavra[::-1])