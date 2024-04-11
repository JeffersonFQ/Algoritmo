# V1 = int(0)
# V2 = 0
# while V1 > -1:
#     V1 = int(input("Digite um número qualquer positivo: "))

#     if V1 % 2 == 0 and V1 > 0:
#         V2 = V1 + V2        
# print("O resultado é: ", V2)

# ----------------------------------------------------------------------- #

# V2 = int(0)
# V1 = int(input("Digite um número; "))
# while V1 != 0:
#     V2 = V2 + V1
#     V1 = int(input("digite outro número: "))
# print("Valor total da soma é: ", V2)

# ----------------------------------------------------------------------- #

# t = 0
# for x in range(10):
#     n = int(input("digite um número: "))
#     if n % 2 == 0:
#         t = t + 1
# print("O total de números pares é: ",t)

# ----------------------------------------------------------------------- #

# t = 0
# for x in range(10):
#     n = int(input("digite um número: "))
#     if n % 2 == 1:
#         t = t + 1
# print("O total de números impares é: ",t)

# ----------------------------------------------------------------------- #

# t = 0
# for x in range(10):
#     n = int(input("digite um número: "))
#     if n >= 0 and n <= 100:
#         t = t + 1
# print("O total de números entre 0 e 100 é: ",t)

# ----------------------------------------------------------------------- #

t = 0
t1 = 0
t2 = 0
t3 = 0
for x in range(10):
    n = int(input("digite um número: "))
    if n >= 0 and n <= 100:
        t = t + 1
    elif n >= 101 and n <= 200:
        t1 = t1 + 1
    elif n > 200:
        t2 = t2 + 1
    else:
        t3 = t3 + 1        
print(f"O total de números entre 0 e 100 é {t}, entre 101 e 200 é {t1}, maiores que 200 é {t2}, e foram digitados outros {t3} numeros fora dessa condição.")