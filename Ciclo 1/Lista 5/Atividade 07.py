# Crie um algoritmo que, dado três números informados pelo usuário, verifique se algum deles é múltiplo 
# de outro. Note que pode haver mais de um múltiplo entre eles.

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
N3 = int(input("Digite o terceiro número: "))
if N1 % N2 == 0 or N1 % N3 == 0:
        print(f"{N1} é múltiplo de {N2} ou {N3}.")
if N2 % N1 == 0 or N2 % N3 == 0:
    print(f"{N2} é múltiplo de {N1} ou {N3}.")
if N3 % N1 == 0 or N3 % N2 == 0:
    print(f"{N3} é múltiplo de {N1} ou {N2}.")