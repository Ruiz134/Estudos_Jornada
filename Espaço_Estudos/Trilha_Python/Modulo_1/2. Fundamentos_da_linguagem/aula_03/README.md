
<details>
<summary><b>Exercício 1: Verificação de Qualidade de Dados</b></summary>

Você está analisando um conjunto de dados de vendas e precisa garantir 
que todos os registros tenham valores positivos para `quantidade` e `preço`. 
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
forem positivos ou "Dados inválidos" caso contrário.

```python
quantidade = 50
preco = 150

if quantidade > 0 and preco > 0:
    print("Dados Válidos")
else:
    print("Dados Inválidos")
```

</details>

<details>
<summary><b>Exercício 2: Classificação de Dados de Sensor</b></summary>

Imagine que você está trabalhando com dados de sensores IoT. 
Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
Baixa: Abaixo de 18°C.
Normal: Entre 18°C e 30°C (inclusive).
Alta: Acima de 30°C.

```python
temperatura = 16

if temperatura > 30:
    print('Temperatura: Alta')
elif  18 <= temperatura <= 30:
    print('Temperatura: Normal')
else:
    print('Temperatura: Baixa')
```

</details>

<details>
<summary><b>Exercício 3: Filtragem de Logs por Severidade</b></summary>

Você está analisando logs de uma aplicação e precisa filtrar mensagens 
com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

```python
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
```

</details>

<details>
<summary><b>Exercício 4: Validação de Dados de Entrada</b></summary>

Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
fornecido um email válido. Escreva um programa que valide essas condições 
e imprima "Dados de usuário válidos" ou o erro específico encontrado.

```python
try:

    idade = int(input('Insira a sua idade: '))
    if not 18 <= idade <=65:
        raise ValueError('Sua idade deve ser entre 18 e 65 anos!')
    else:
        email = input('Insira seu melhor email: ')
        if not '@' in email or not email.endswith('.com'):
            raise ValueError('Insira um e-mail válido!')
        else:
            print(f'>>> Os Dados do Usuário são Válidos <<<\nEmail: {email}\nIdade: {idade}')

except ValueError as e:
    print(f'[ERRO]: {e}')
```

</details>

<details>
<summary><b>Exercício 5: Detecção de Anomalias em Dados de Transações</b></summary>

Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

```python
try:
    transacao = {'valor': 12000, 'hora': 20}

    if transacao['valor'] > 10000 or 9 > transacao['hora'] > 18:
        raise ValueError('Transação Suspeita')
    else: 
        print('Transação Ok!')
except ValueError as e:
    print(f'[ERRO] {e}')
```

</details>

<details>
<summary><b>Exercício 6. Contagem de Palavras em Textos</b></summary>

Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

```python
# texto = input('Insira um texto: ')
texto = '"o doce perguntou ao doce qual é o doce mais doce que o doce de batata doce'

lista_texto = texto.split()

dicionario = {}

for palavra in lista_texto:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print(dicionario)
```

</details>

<details>
<summary><b>Exercício 7. Normalização de Dados</b></summary>

$$x' = \frac{x - \text{min}(X)}{\text{max}(X) - \text{min}(X)}$$

Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
`numeros = [10, 20, 30, 40, 50]`

```python
numeros = [10, 20, 30, 40, 50]

min_val = min(numeros)
max_val = max(numeros)
numeros_normalizados = []

for x in numeros:

    resultado = (x - min_val) / (max_val - min_val)
    numeros_normalizados.append(resultado)

print(numeros_normalizados)
```

</details>

<details>
<summary><b>Exercício 8. Filtragem de Dados Faltantes</b></summary>

Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

``  {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
``

```python
dados = [    
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

for user in dados:
    nome = user['nome']
    if user['email'] == "":
        print(f'Usuário com email não cadastrado é: {nome}')
```

</details>

<details>
<summary><b>Exercício 9. Extração de Subconjuntos de Dados</b></summary>

Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

```python
numeros = range(1, 11)
lista_pares = []

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
print(lista_pares)  
```

</details>

<details>
<summary><b>Exercício 10. Agregação de Dados por Categoria</b></summary>

Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

```python
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]

    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)
```

</details>


## Exercícios com WHILE


<details>
<summary><b>Exercício 11. Leitura de Dados até Flag</b></summary>

Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

```python
entrada = ""

try:

    while entrada.lower() != 'sair':
        entrada = input('Digite um valor. Atenção! Para sair escreva "Sair" ')
        if entrada.lower() == 'sair':
            raise KeyboardInterrupt('Usuário encerrou a operação!')
        
except KeyboardInterrupt as k:
    print(f'[FIM] {k}')
                                
```

</details>

<details>
<summary><b>Exercício 12. Validação de Entrada</b></summary>

Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

```python
entrada = 0
minimo = 5
maximo = 10

try:
    while entrada <= minimo or entrada >= maximo:
        
        entrada = int(input('Digite um valor. Atenção! Entrada Válida de 5 a 10 somente! '))

        if entrada >= minimo or entrada <= maximo:
            raise KeyboardInterrupt('Usuário encerrou a operação!')
        
except KeyboardInterrupt as k:
    print(f'[FIM] {k}')   
```

</details>

<details>
<summary><b>Exercício 13. Consumo de API Simulado</b></summary>

Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

```python
pagina_atual = 1
paginas_totais = 5 

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
 
    pagina_atual += 1

print("Páginas processadas!")
```

</details>

<details>
<summary><b>Exercício 14. Tentativas de Conexãos</b></summary>

Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

```python
tentativas_maximas = 5
tentativa = 1
senha = input('Insira a senha de conexão: ')

while tentativa <= tentativas_maximas or senha == '123':

    senha = input(f'Insira a senha de conexão {tentativa} de {tentativas_maximas} : ')

    if senha == '123':
        print('Conexão Realizada!')
        break
    else:
        tentativa += 1

        if tentativa == 6:
            print('Conexão Bloqueada!')
```

</details>

<details>
<summary><b>Exercício 15. Processamento de Dados com Condição de Parada</b></summary>

Processar itens de uma lista até encontrar um valor específico que indica a parada.

```python
itens = [1, 2, 3, "parar", 4, 5]

i = 0

while i < len(itens):
    if itens[i] == "parar":
        print("Processo encerrado")
        break
    print(f"Processando item: {itens[i]}")

    i += 1
```

</details>
