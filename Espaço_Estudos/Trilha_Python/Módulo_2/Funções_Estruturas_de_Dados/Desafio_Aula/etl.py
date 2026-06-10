import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida os json

def extrair_dados_e_consolidar(path: str)-> pd.DataFrame:
    '''
     Lê todos os arquivos JSON de uma pasta e os consolida em um único DataFrame.

    Args:
        path (str): Caminho da pasta contendo os arquivos JSON.

    Returns:
        pd.DataFrame: DataFrame consolidado com os dados dos arquivos JSON.
    '''

    read_files = glob.glob(os.path.join(path,"*.json"))
    df = [pd.read_json(arquivo) for arquivo in read_files]
    df = pd.concat(df, ignore_index=True)
    return df

# uma funcao que transforma
def calcular_total_vendas(df_extraido: pd.DataFrame) -> pd.DataFrame:
    '''
    Calcula o total de vendas multiplicando a quantidade pelo valor da venda.

    Args:
        df_extraido (pd.DataFrame): DataFrame com os dados de vendas.

    Returns:
        pd.DataFrame: DataFrame com a coluna "total" adicionada.
    '''
    df_extraido["total"] = df_extraido["Quantidade"] * df_extraido["Venda"]
    return df_extraido


# uma funcao que da load em csv ou parquet
def carregar_dados_em_csv_ou_parquet(format_saida: int, df_saida: pd.DataFrame) -> None:
    '''
    Carrega os dados em um arquivo CSV ou Parquet.

    Args:
        format_saida (int): Formato de saída. 1 para CSV, 2 para Parquet.
        df_saida (pd.DataFrame): DataFrame com os dados a serem carregados.

    Returns:
        None
    '''
    if format_saida == 1:
        df_saida.to_csv("data.csv", index=False)
        print("Arquivo CSV gerado com sucesso!")
    elif format_saida == 2:
        df_saida.to_parquet("data.parquet", engine="pyarrow", index=False)
        print("Arquivo Parquet gerado com sucesso!")
    else:
        print("Formato inválido! Escolha entre CSV (1) ou Parquet (2)")
    return None


def pipeline_gerar_calculo_vendas(pasta_de_dados: str, formato_de_saida: int = 1):
    '''
    Executa o pipeline de ETL completo.

    Args:
        pasta_de_dados (str): Caminho da pasta contendo os arquivos JSON.
        formato_de_saida (int): Formato de saída. 1 para CSV, 2 para Parquet.

    Returns:
        None
    '''
    extração_df = extrair_dados_e_consolidar(pasta_de_dados)
    transformação_df = calcular_total_vendas(extração_df)
    carregar_dados_em_csv_ou_parquet(formato_de_saida, df_saida=transformação_df)
    return None

    