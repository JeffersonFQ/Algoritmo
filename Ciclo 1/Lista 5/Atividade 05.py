# Agora altere o algoritmo anterior de maneira que ele verifique também se o nível informado está entre 0 
# e 10. Caso contrário uma mensagem de erro deve ser apresenta

A = int(input("Qual o nível de alerta (0 - 10): "))
if A > 9 and A >= 0 and A <= 10:
    print("Alerta GRAVE!!! ")
else:
    print("ERROR: Número informado incorreto! ")