mes = int(input("Informe o número do mês: "))

if mes == 1:
    nome = "janeiro"
elif mes == 2:
    nome = "fevereiro"
elif mes == 3:
    nome = "março"
elif mes == 4:
    nome = "abril"
elif mes == 5:
    nome = "maio"
elif mes == 6:
    nome = "junho"
elif mes == 7:
    nome = "julho"
elif mes == 8:
    nome = "agosto"
elif mes == 9:
    nome = "setembro"
elif mes == 10:
    nome = "outubro"
elif mes == 11:
    nome = "novembro"
elif mes == 12:
    nome = "dezembro"
else:
    print("Mês inválido")
    exit()

trimestre = (mes - 1) // 3 + 1

print("O mês de", nome, "é do", trimestre, "º trimestre do ano")