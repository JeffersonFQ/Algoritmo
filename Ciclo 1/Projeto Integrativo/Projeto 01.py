# Implementar, em linguagem Python, uma parte específica do seu Projeto Integrativo que envolva a 
# aplicação de estruturas condicionais.


def verificar_doador(idade, peso, ultima_doacao):
# Define uma função para verificar a compatibilidade do doador.
    if idade < 18 or idade > 60:
        return "Infelizmente você não é elegível para doar sangue ainda, devido à sua idade."
    elif peso < 50:
        return "Infelizmente você não é elegível para doar sangue ainda, devido ao seu peso."
    elif ultima_doacao < 3:
        return "Infelizmente você não é elegível para doar sangue ainda, devido ao tempo desde a sua última doação."
    else:
        return "Parabéns!! Você é elegível para doar sangue. Agradeçemos sua vontade de ajudar!"

idade = int(input("Por favor, digite a sua idade: "))
# Entrada para a idade.

peso = float(input("Por favor, digite o seu peso: "))
# Entrada para o peso.

ultima_doacao = int(input("Quanto tempo faz desde sua ultima doação (Em meses): "))
# Entrada para o periodo da ultima doação.

print(verificar_doador(idade, peso, ultima_doacao))
# Print com retorno da função de verificação.
