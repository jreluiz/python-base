#!/usr/bin/env python3
""" Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operacao: sum
n1: 5
n2 4
"""
__version__ = "0.1.0"
__author__ = "Jorge Luiz"
__license__ = "Unlicense"

import os
import sys

argumentos = sys.argv[1:]

# TODO: Exceptions
if not argumentos:
    op = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    argumentos = [op, n1, n2]
elif len(argumentos) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

op, *nums = argumentos
operacoes_validas = ["sum", "sub", "mul", "div",]

if op not in operacoes_validas:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: repetição com while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1,  n2 = validated_nums

# TODO: Usar dict de funções
if op == "sum":
    resultado = n1 + n2
elif op == "sub":
    resultado = n1 - n2
elif op == "mul":
    resultado = n1 * n2
elif op == "div":
    resultado = n1 / n2
    
print(resultado)

                 

        
        
