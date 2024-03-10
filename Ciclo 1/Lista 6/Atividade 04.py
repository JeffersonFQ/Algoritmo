# Escreva um algoritmo para cadastro de dados básicos de alunos. O usuário deve informar o número da 
# matrícula (cinco dígitos), nome completo do aluno, gênero (o usuário deve informar “M” ou “F”), curso 
# (o usuário deve informar “BES”, “BEC” ou “ADS”) e coeficiente de rendimento (dever ser maior ou igual 
# a zero e menor ou igual a 100). Como resultado o sistema deve imprimir a matrícula, o nome do aluno, 
# gênero (deve imprimir “Masculino” ou “Feminino”), curso (“Bacharelado em Engenharia de Software” 
# para “BES”, “Bacharelado em Engenharia de Computação” para “BEC” e “Analise e Desenvolvimento 
# de Sistemas” para “ADS”), o coeficiente de rendimento, seguido por “Excelente” se o coeficiente for [90, 
# 100], “Bom” se entre [70, 90), “Regular” se entre [50, 70), “Necessita melhoras” se entre [30, 50) e 
# “Preocupante” se entre [0, 30). Note a existência de intervalos fechados e semifechados para os 
# coeficientes.

Matricula = int(input("Informe o número da matrícula: "))
Nome = str.title(input("Informe o nome completo do aluno: "))
Genero = str.lower(input("Informe o gênero do Aluno (M/F): "))
Curso = str.upper(input("Informe o curso do aluno (BES, BEC ou ADS): "))
CRendimento = float(input("Informe o coeficiente de rendimento: "))

if Genero == "m":
    Genero = "Masculino"
elif Genero == 'f':
    Genero = "Feminino"
else:
    Genero = 'Gênero inválido.'

match Curso:
    case 'BES':
        Curso = 'Bacharelado em Engenharia de Software'
    case 'BEC':
        Curso = 'Bacharelado em Engenharia da Computação'
    case 'ADS':
        Curso = 'Analise e Desenvolvimento de Sistemas'
    case _:
        Curso = 'Curso inválido'

if CRendimento <= 100 and CRendimento >= 90:
    CRm = 'Excelente'
elif CRendimento < 90 and CRendimento >= 70:
    CRm = 'Bom'
elif CRendimento < 70 and CRendimento >= 50:
    CRm = 'Regular'
elif CRendimento < 50 and CRendimento >= 30:
    CRm = 'Necesita melhoras'
elif CRendimento < 30 and CRendimento >= 0:
    CRm = 'Preocupante'
else:
    CRm = 'Coeficiente inválido'

print("\nDados do aluno:")
print(f"Matrícula: {Matricula}")
print(f"Nome: {Nome}")
print(f"Gênero: {Genero}")
print(f"Curso: {Curso}")
print(f"Coeficiente de Rendimento: {CRendimento} - {CRm}")