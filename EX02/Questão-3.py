valores = []

for i in range(4):
    numero = int(input("Digite um valor inteiro: "))

    if numero in valores:
        print("Erro: os valores devem ser diferentes.")
        exit()

    valores.append(numero)

valores.sort()

print("Maior valor =", valores[3])
print("Menor valor =", valores[0])
print("A soma do segundo maior valor com o segundo menor =", valores[1] + valores[2])