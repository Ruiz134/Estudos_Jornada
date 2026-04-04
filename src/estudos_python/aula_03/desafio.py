nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:  
    try:
        
        nome: str = input("Digite o seu nome: ").strip()
        if not nome:
            raise ValueError("Valor Vazio. Gentileza Preencher com valores inteiros")
        elif not nome.replace(" ", "").isalpha():
            raise ValueError("Valor Inválido no Campo Nome. Gentileza inserir nome em formato de texto")
        else:
            nome_valido = True

    except ValueError as e:
        print(f"[ERRO]: {e}")
    
while salario_valido is not True:
    try:
        salario = input("Digite o valor do seu salário: ").strip()
        if not salario:
            raise ValueError("Valor Vazio. Gentileza Preencher com valores inteiros")
        elif not salario.isdigit():
            raise ValueError("Valor Inválido no Campo Salario. Gentileza inserir salario em formato de numero")
        else:
            salario_valido = True
        salario_int = int(salario)

    except ValueError as e:
        print(f"[ERRO]: {e}")

while bonus_valido is not True:  
    try:
        bonus = input("Insira o valor do bonus: ").strip()
        if not bonus:
            raise ValueError("Valor Vazio. Gentileza Preencher com valores inteiros")    
        elif not bonus.isdigit():
            raise ValueError("Valor Inválido no Campo bonus. Gentileza inserir bonus em formato de numero")
        else:
             bonus_valido = True
        bonus_int = int(bonus)

    except ValueError as e:
        print(f"[ERRO]: {e}")

bonus_final: int = 1000 + salario_int + bonus_int
print(bonus_final)

print(f"O {nome} recebeu um salario de {salario} e um bonus de {bonus}% e obteve no final um bonus total de {bonus_final}")