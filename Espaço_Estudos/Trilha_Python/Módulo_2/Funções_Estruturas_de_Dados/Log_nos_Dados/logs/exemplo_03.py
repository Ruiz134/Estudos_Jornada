''' Neste exemplo:

Utilizei o Decorador log_decorador para gerar o log da função soma.

'''
import sys
import os
from loguru import logger

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "Decoradores"
))

from utils_log import log_decorator

@log_decorator
def soma(x: int, y: int):
    try:
        logger.info(f"Iniciando a soma de {x} e {y}")
        logger.info("Realizando a operação")
        resultado = x + y
        logger.info(f"O resultado da soma é {resultado}")
        return resultado

    except Exception as e:
        logger.critical(f"Erro ao somar: {e}")

soma( 10, "2" )


