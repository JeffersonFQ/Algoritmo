# Considerando o sistema de notas da UniEVANGÉLICA, construa um algoritmo que, dadas 4 notas 
# parciais de um aluno pelo usuário, calcule a média e imprima se o aluno foi aprovado ou reprovado. 
# Considere os 3 ciclos

VA = float(input("Digite a nota da Atividade Avaliativa (0 - 60): "))
PRI = float(input("Digite a nota do projeto integrativo (0 - 20): "))
ARP = float(input("Digite a nota total da ARP (0 - 10): "))
APS = float(input("Digite a nota total das APSs (0 - 10): "))
M = VA + PRI + ARP + APS
MF = M/3
if M >= 60:
    print(f"Aluno aprovado no ciclo com média {M}.")
else:
    print(f"Aluno com nota abaixo da média no ciclo({M})")
if MF >= 60:
    print(f"Aluno aprovado no curso com média final {MF}.")
else:
    print(f"Aluno reprovado no curso com média final {MF}.")
    