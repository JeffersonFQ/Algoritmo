# Crie um algoritmo que, dados o tamanho de três lados informados pelo usuário, verifique se: (1) é um 
# triângulo isósceles, (2) é equilátero, (3) é escaleno ou (4) não é um triângulo.

L1 = int(input("Digite o valor do primeiro lado: "))
L2 = int(input("Digite o valor do segundo lado: "))
L3 = int(input("Digite o valor do terceiro lado: "))
if L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    if L1 == L2 == L3:
        print("O triângulo é equilátero.")
    elif L1 == L2 or L2 == L3 or L3 == L1:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Esses valores não forma um triângulo. ")