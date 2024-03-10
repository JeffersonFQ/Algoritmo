# Você viajou para os Estados Unidos e descobriu que lá a unidade de medida de temperatura é diferente 
# da do Brasil. Para não ter que acessar um serviço na internet a todo o momento, nem fazer os cálculos 
# manualmente, faça um algoritmo que converte a temperatura, dada uma unidade de medida e uma 
# temperatura. Ou seja, se a data for informada em Celsius o algoritmo deve fornecer a temperatura em 
# Fahrenheit, já se a temperatura for fornecida em Fahrenheit, o resultado deve ser em graus Celsius.

while True:
    U = str.upper(input("Informe a unidade de medida (C para Celsius, F para Fahrenheit): "))
    if U not in ['C', 'F']:
        print("Por favor, insira 'C' para Celsius ou 'F' para Fahrenheit.")
        continue
    else:
        break
T = float(input("Informe a temperatura: "))
if U == 'C':
    R1 = (T * 9/5) + 32
    R2 = 'Fahrenheit'
else:
    R1 = (T - 32) * 5/9
    R2 = 'Celsius'

print(f"A temperatuda convertida é de {R1}° {R2}")
