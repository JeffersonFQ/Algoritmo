# Faça um algoritmo que, dados três números inteiros, os imprima em ordem crescente.

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
N3 = int(input("Digite o terceiro número: "))
L = [N1, N2, N3]
L.sort()
print(f"A ordem dos número digitados é {L}")
