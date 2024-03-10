# Escreva um programa que, dado o valor da venda, imprima a comissa ̃o que devera ́ ser paga ao 
# vendedor. Para calcular a comissa ̃o, considere a tabela da lista:

valor = float(input("Valor total da venda R$"))
if valor >= 100000:
    C = (valor * 0.16) + 700
elif valor < 100000 and valor >= 80000:
    C = (valor * 0.14) + 650
elif valor < 80000 and valor >= 60000:
    C = (valor * 0.14) + 600
elif valor < 60000 and valor >= 40000:
    C = (valor * 0.14) + 550
elif valor < 40000 and valor >= 20000:
    C = (valor * 0.14) + 500
elif valor < 2000:
    C = (valor * 0.14) + 400
else:
    C = 0
print(f"O Valor de comissão da venda de R${valor:.2f} é de R${C:.2f}")