def Diagonal(b, h):
    return (b * 2 + h * 2) ** 0.5


b = float(input("Digite a base: "))
h = float(input("Digite a altura: "))

print("Diagonal =", Diagonal(b, h))