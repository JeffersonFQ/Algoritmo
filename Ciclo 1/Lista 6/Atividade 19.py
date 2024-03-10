# Faça um algoritmo que, dado o valor total em reais e o número de prestações desejadas, calcule o valor 
# de cada prestação. O número mínimo de prestações deve ser 12. Se o número de prestações for maior 
# ou igual a 24, adicione 10% de juros ao valor total, se for maior ou igual a 36, adicione 15% de juros ao 
# valor total.

Valor = float(input("Digite o valor desejado: "))
while True:
    Prestacao = float(input("Digite o número de prestações (Mínimo 12x):"))
    if Prestacao < 12:
        print("Por favor, insira um valor maior ou igual a 12: ")
        continue
    else:
        break
if Prestacao >= 36:
    Total = (Valor * 1.15) / Prestacao
elif Prestacao >= 24:
    Total = (Valor * 1.1) / Prestacao
else:
    Total = Valor / Prestacao
confirmacao = str.lower(input(f"A proposta ficaria em {Prestacao:.0f}x de R${Total:.2f}, podemos continuar?(s/n) "))
if confirmacao == 's':
    print("Acordo fechado! ")
else:
    print("Vamos tentar novamente.")