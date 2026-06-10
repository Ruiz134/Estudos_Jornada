import csv

# Ler Arquivos CSV sem a Biblioteca Pandas.
def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    '''
    Lê um arquivo CSV e retorna uma lista de dicionários com os dados.

    Args:
        nome_do_arquivo_csv (str): Caminho do arquivo CSV.

    Returns:
        list[dict]: Lista de dicionários com os dados do arquivo CSV.
    '''
    dados = []
    with open(nome_do_arquivo_csv, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados

# Calcular Total de Vendas sem usar Pandas
def calcular_total_vendas(lista_vendas: list[dict]) -> list[dict]:
    '''
    Calcula o total de vendas multiplicando a quantidade pelo valor da venda.

    Args:
        lista_vendas (list[dict]): Lista de dicionários com os dados de vendas.

    Returns:
        list[dict]: Lista de dicionários com a coluna "total" adicionada.
    '''
    lista_vendas_calculada = []
    for linha in lista_vendas:
        linha["total_2"] = int(linha["Quantidade"]) * float(linha["Venda"])
        linha["total_2"] = int(linha["total_2"])
        lista_vendas_calculada.append(linha)
    return lista_vendas_calculada

# Salvando Arquivo no diretório data
def salvar_dados_em_csv(dados: list[dict], nome_do_arquivo_csv: str):
    '''
    Salva os dados em um arquivo CSV.

    Args:
        dados (list[dict]): Lista de dicionários com os dados a serem salvos.
        nome_do_arquivo_csv (str): Caminho do arquivo CSV onde os dados serão salvos.
    '''
    with open(nome_do_arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=dados[0].keys())
        escritor.writeheader()
        escritor.writerows(dados)
    return None

def pipeline_gerar_calculo_vendas(path_arquivo: str, nome_do_arquivo_csv: str):
    '''
    Executa o pipeline completo de ETL.

    Args:
        path_arquivo (str): Caminho do arquivo CSV.
        nome_do_arquivo_csv (str): Caminho do arquivo CSV onde os dados serão salvos.
    '''

    lista_de_produtos = ler_csv(path_arquivo)
    calcular_vendas = calcular_total_vendas(lista_de_produtos)
    salvar_dados_em_csv(calcular_vendas, nome_do_arquivo_csv)
    return None
