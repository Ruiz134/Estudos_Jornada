''' Neste exemplo:

1. Configurei o Logger para capturar somente mensagens do tipo CRITICAL e adicioná-lo ao log. 
2. Usei a lib "os" para criar o caminho do arquivo .log de forma automatizada. 

'''

from loguru import logger
import os

caminho_log = os.path.join(
    "Espaço_Estudos", "Trilha_Python", "Módulo_2",
    "Funções_Estruturas_de_Dados", "Log_nos_Dados", "logs", "meu_log.log"
)

logger.add(
        caminho_log, 
        level="CRITICAL"
    )


def soma(x: int, y: int):
    try:
        logger.info(f"Iniciando a soma de {x} e {y}")
        logger.info("Realizando a operação")
        resultado = x + y
        logger.info(f"O resultado da soma é {resultado}")
        return resultado

    except Exception as e:
        logger.critical(f"Erro ao somar: {e}")

soma( 10, 2 )


