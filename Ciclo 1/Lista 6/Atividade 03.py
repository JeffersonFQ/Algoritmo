# Agora altere esse algoritmo para que imprima os números em ordem decrescente.

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
N3 = int(input("Digite o terceiro número: "))
L = [N1, N2, N3]
L.sort(reverse=True)
print(f"A ordem dos número digitados é {L}")
