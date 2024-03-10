# Agora, crie um algoritmo que imprima o dia anterior da data informada.

dia_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    dia_mes[2] = 29

if dia == 1:
    if mes == 1:
        dia = 31
        mes = 12
        ano -= 1
    else:
        mes -= 1
        dia = dia_mes[mes]
else:
    dia -= 1

print(f"O dia seguinte é: {dia}/{mes}/{ano}")