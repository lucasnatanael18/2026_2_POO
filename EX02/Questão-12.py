def MenorInteiro(x):
    inteiro = int(x)

    if x == inteiro:
        return inteiro
    else:
        return inteiro + 1


x = float(input("Digite um número real: "))

print(MenorInteiro(x))