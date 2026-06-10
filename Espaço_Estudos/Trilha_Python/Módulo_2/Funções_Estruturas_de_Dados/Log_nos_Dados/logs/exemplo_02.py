''' Neste exemplo:

1. Configurei o Logger para capturar o usuário ativo do Windows e adicioná-lo ao log. 
2. Fiz isso customizando o formato da mensagem e injetando parâmetros extras, 
permitindo que o arquivo .log registre o contexto do usuário de forma automatizada.

'''

from loguru import logger
import os
import getpass

username = getpass.getuser()

caminho_log = os.path.join(
    "Espaço_Estudos", "Trilha_Python", "Módulo_2",
    "Funções_Estruturas_de_Dados", "Log_nos_Dados", "logs", "meu_log.log"
)

logger.configure(extra={"user": username})

logger.add(
    caminho_log,
    format="{time: DD.MM.YYYY HH:mm:ss} | {level} | User: {extra[user]} | Descrição: {message}",
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


