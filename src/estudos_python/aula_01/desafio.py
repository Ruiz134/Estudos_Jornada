

### Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal
# e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome 
# e informando o valor do salário em comparação com o bônus recebido.

# Instruções:
# O programa deve começar solicitando ao usuário que insira seu nome.
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Insira o valor do bonus: "))

# 4) Calcule o valor do bônus final

bonus_final = 1000 + salario + bonus

# 5) Imprima cálculo do KPI para o usuário
print(bonus_final)
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O {nome} recebeu um salario de {salario} e um bonus de {bonus} e obteve no final um bonus total de {bonus_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?