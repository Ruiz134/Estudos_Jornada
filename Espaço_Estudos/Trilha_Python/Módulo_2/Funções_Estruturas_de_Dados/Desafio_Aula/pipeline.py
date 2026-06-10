import sys
import os

# Adiciona a pasta do próprio script ao sys.path (garante o import do etl.py mesmo rodando de fora da pasta principal)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from etl import pipeline_gerar_calculo_vendas

# Insira o caminho dos Dados:
dados: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# Insira o formato de saida, sendo (1) para CSV e (2) para Parquet
formato: int = 2
pipeline_gerar_calculo_vendas(pasta_de_dados=dados, formato_de_saida=formato)
