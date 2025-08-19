#!/usr/bin/env python3

import os
import logging
from logging import handlers
import antigravity

# TODO: usar função
# TODO: usar a lib loguru

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

#instância
log = logging.Logger("logs.py", log_level)

#level
#ch = logging.StreamHandler()  # manda para o console/terminal/stderr
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(  # salvar log em arquivo
    "meu_log.log",
    maxBytes=300,    # interessante usar 10**6 = 1MB
    backupCount=10,  # cria até 10 arquivos
)

#formatacao
fmt = logging.Formatter("%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s")
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

#destino
#log.addHandler(ch)
log.addHandler(fh)

log.debug("Mensagem para o dev")
log.info("Mensagens gerais para os usuários")
log.warning("Aviso que não causa erros")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral, por ex banco sumiu")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
