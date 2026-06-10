from etl_antigo import pipeline_gerar_calculo_vendas


path_arquivo: str = "data.csv"
name_arquivo: str = "data_calculada.csv"

pipeline_gerar_calculo_vendas(path_arquivo, name_arquivo)