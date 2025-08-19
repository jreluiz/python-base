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

# print(f"{sys.argv=}")

# sempre no padrão snack case
arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print("Opção inválida `{key}`")
        sys.exit()
    # print(key, value)
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: usar repetição
    if current_language is None:
        current_language = input("Digite a linguagem: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))

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
