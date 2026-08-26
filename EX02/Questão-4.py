data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data.split("/"))

valido = True

if ano < 1900 or ano > 2100:
    valido = False

elif mes < 1 or mes > 12:
    valido = False

else:
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
        dias = 29
    else:
        dias = dias_mes[mes - 1]

    if dia < 1 or dia > dias:
        valido = False

if valido:
    print("A data informada é válida")
else:
    print("A data informada não é válida")