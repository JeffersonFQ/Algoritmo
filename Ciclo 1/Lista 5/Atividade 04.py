# Crie um algoritmo que, dado o nível de alerta de risco, imprima se ele for GRAVE. O nível de alerta é
# um número que varia de 0 a 10. O nível é considerado GRAVE quando ele é superior a 9.

A = int(input("Qual o nível de alerta (0 - 10): "))
if A > 9:
    print("Alerta GRAVE!!! ")
elif A > 5 and A < 9:
    print("Alerta moderado! ")
else:
    print("Alerta Baixo. ")