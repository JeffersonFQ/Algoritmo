# Crie um algoritmo que, dado três números informados pelo usuário, informe qual é o maior deles.

N1 = int(input("Digite o primeiro número: "))
R1 = N1
R2 = "Primeiro"
N2 = int(input("Digite o segundo número: "))
if N2 > N1:
    R1 = N2
    R2 = "Segundo"
N3 = int(input("Digite o terceiro número: "))
if N3 > N2 and N3 > N1:
    R1 = N3
    R2 = "Terceiro"
print(f"O {R2} valor ({R1}) é maior")



