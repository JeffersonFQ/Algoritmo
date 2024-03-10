# Problemas simples do cotidiano podem representar desafios para o mundo computacional. Faça um 
# algoritmo que, dados três números inteiros representando dia, mês e ano de uma data, imprima qual o 
# dia seguinte.

dia_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    dia_mes[2] = 29

if dia == dia_mes[mes]:
    dia = 1
    if mes == 12:
        mes = 1
        ano += 1
    else:
        mes += 1
else:
    dia += 1

print(f"O dia seguinte é: {dia}/{mes}/{ano}")
