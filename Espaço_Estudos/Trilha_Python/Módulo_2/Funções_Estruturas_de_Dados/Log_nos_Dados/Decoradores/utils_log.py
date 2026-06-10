from loguru import logger
from sys import stderr
from functools import wraps
import os
import getpass

username = getpass.getuser()

caminho_log = os.path.join(
    "Espaço_Estudos", "Trilha_Python", "Módulo_2",
    "Funções_Estruturas_de_Dados", "Log_nos_Dados", "logs", "meu_log.log"
)

logger.configure(extra={"user": username})

logger.remove()

logger.add(
    sink=stderr,
    format="<level> {time: DD.MM.YYYY HH:mm:ss} </level>| <level> User: {extra[user]} </level> | <level> {level} </level> | <level> Descrição: {message} </level>",
    level="CRITICAL"
)

logger.add(
    caminho_log,
    format="{time: DD.MM.YYYY HH:mm:ss} | User: {extra[user]} | {level} | Descrição: {message} ",
    level="CRITICAL"
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  
    return wrapper



