'''
Exemplo Simples utilizando Logger
'''

from loguru import logger

logger.add(r"Espaço_Estudos\Trilha_Python\Módulo_2\Funções_Estruturas_de_Dados\Log_nos_Dados\logs\meu_log.log")

def soma(x: int, y: int):
    logger.info(f"Iniciando a soma de {x} e {y}")
    logger.info("Realizando a operação")
    return x + y

logger.info(f"O resultado da soma é {soma(2, 3)}")


