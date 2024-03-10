# Crie um algoritmo que, dados os lados de um triângulo informados pelo usuário, calcule a área

L1 = int(input("Digite o valor do primeiro lado: "))
L2 = int(input("Digite o valor do segundo lado: "))
L3 = int(input("Digite o valor do terceiro lado: "))
if L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    if L1 == L2 == L3:
        print("O triângulo é equilátero.")
        A = (L1 * L2 * 1.732)/4
        print(f"e a área do triângulo é {A}")
    elif L1 == L2 or L2 == L3 or L3 == L1:
        print("O triângulo é isósceles.")
        B = int(input("Qual valor da base do triângulo: "))
        H = int(input("Qual valor da altura do triângulo: "))
        A = (B * H)/2
        print(f"e a área do triângulo é {A}")
    else:
        print("O triângulo é escaleno.")
        B = int(input("Qual valor da base do triângulo: "))
        H = int(input("Qual valor da altura do triângulo: "))
        A = (B * H)/2
        print(f"e a área do triângulo é {A}")
else:
    print("Esses valores não forma um triângulo. ")