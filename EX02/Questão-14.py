
def MMC(x, y):
    maior = max(x, y)

    while maior % x != 0 or maior % y != 0:
        maior += 1

    return maior


x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print("MMC =", MMC(x, y))