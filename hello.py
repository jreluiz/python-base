#!/usr/bin/env python3
"""
Hello World Multi Linguas

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"   # Dunder
__author__ = "Jorge Luiz"
__license__ = "Unlicense"

import os
import sys

print(f"{sys.argv=}")

# sempre no padrão snack case
current_language = os.getenv("LANG", "en_US")[:5]   # usando fatiamento em python

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])

# msg = "Hello, World!"
# 
# if current_language == "pt_BR":
#     msg = "Olá Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language = "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde!"

# print é uma biblioteca built-in
# print(msg)   
