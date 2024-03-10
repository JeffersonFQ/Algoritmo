# Agora altere o algoritmo anterior de maneira que ele verifique os demais níveis de alerta. Considere: 0-
# 3 é "BAIXO", maior que 3 até 6 "MÉDIO", maior que 6 até 9 "ALTO", para os demais casos é considerado 
# "GRAVE".

A = int(input("Qual o nível de alerta (0 - 10): "))
if A > 9 and A >= 0 and A <= 10:
    print("Alerta GRAVE!!! ")
elif A > 6 and A <= 9:
    print("Alerta ALTO!! ")
elif A > 3 and A <= 7:
    print("Alerta Médio! ")
elif A >= 0 and A <= 3:
    print("Alerta Baixo. ")
else:
    print("ERROR: Número informado incorreto! ")