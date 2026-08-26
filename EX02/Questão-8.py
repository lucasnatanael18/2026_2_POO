frase = input("Digite uma frase: ")

for i in range(len(frase)):
    print(frase[i:] + frase[:i])