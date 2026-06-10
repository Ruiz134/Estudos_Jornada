'''
Neste exemplo, eu vejo alguns tipos de mensagens de log utilizando loguru:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL
'''
from loguru import logger

logger.debug("Mensagem de debug")
logger.info("Mensagem de info")
logger.warning("Mensagem de warning")
logger.error("Mensagem de erro")
logger.critical("Mensagem de critical")
