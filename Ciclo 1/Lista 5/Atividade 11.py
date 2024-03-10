# Agora altere o algoritmo anterior de maneira que ele permita que o professor, antes de informar as notas, 
# informe os seus respectivos pesos. Depois disso o algoritmo deve, de análoga ao exercício anterior, 
# calcular a média, no entanto, agora considerando os seus pesos. Lembrete: A soma dos pesos das 
# notas sempre deve ser 10.

VA = float(input("Digite a nota da Atividade Avaliativa (0 - 60): "))
PRI = float(input("Digite a nota do projeto integrativo (0 - 20): "))
ARP = float(input("Digite a nota total da ARP (0 - 10): "))
APS = float(input("Digite a nota total das APSs (0 - 10): "))
print("Agora vamos digitar o peso das repectivas notas! ")
PT = 0
while PT != 10:
    P1 = float(input("Digite o peso da primeira nota: "))
    P2 = float(input("Digite o peso da segunda nota: "))
    P3 = float(input("Digite o peso da terceira nota: "))
    P4 = float(input("Digite o peso da quarta nota: "))
    PT = P1 + P2 + P3 + P4
    if PT != 10:
        print("A soma dos pesos deve ser igual a 10. ")
M = (VA  * P1 + PRI * P2 + ARP * P3 + APS * P4)/10
MF = M/3
if M >= 60:
    print(f"Aluno aprovado no ciclo com média {M}.")
else:
    print(f"Aluno com nota abaixo da média no ciclo({M})")
if MF >= 60:
    print(f"Aluno aprovado no curso com média final {MF}.")
else:
    print(f"Aluno reprovado no curso com média final {MF}.")