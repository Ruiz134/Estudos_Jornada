from etl import pipeline_gerar_calculo_vendas

# Insira o caminho dos Dados:
dados: str = "data"

# Insira o formato de saida, sendo (1) para CSV e (2) para Parquet
formato: int = 1
pipeline_gerar_calculo_vendas(pasta_de_dados=dados, formato_de_saida=formato)
