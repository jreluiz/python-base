#!/usr/bin/env python3

import logging

#instância
log = logging.Logger("logs.py", logging.DEBUG)

#level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#formatacao
fmt = logging.Formatter("%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s")
ch.setFormatter(fmt)

#destino
log.addHandler(ch)

log.debug("Mensagem para o dev")
log.info("Mensagens gerais para os usuários")
log.warning("Aviso que não causa erros")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral, por ex banco sumiu")


