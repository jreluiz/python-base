#!/usr/bin/env python
"""Imprime a tabuada de 0 a 10."""

__version__ = "0.1.0"
__author__ = "Jorge"

# numeros = [1,2,3,4,5,6,7,8,9]
numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do: ", numero)
    for numero2 in numeros:
        print(numero * numero2)
