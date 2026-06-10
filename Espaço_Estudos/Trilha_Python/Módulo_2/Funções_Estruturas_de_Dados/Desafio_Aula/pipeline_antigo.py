
from etl_antigo import pipeline_gerar_calculo_vendas


path_arquivo: str = r"Espaço_Estudos\Trilha_Python\Módulo_2\Funções_Estruturas_de_Dados\Desafio_Aula\data\data.csv"
name_arquivo: str = r"Espaço_Estudos\Trilha_Python\Módulo_2\Funções_Estruturas_de_Dados\Desafio_Aula\data\data_calculada.csv"

pipeline_gerar_calculo_vendas(path_arquivo, name_arquivo)