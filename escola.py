#!/usr/bin/env python3
"""Exibe relatório de crianças por atividades.

Imprimir a lista de crianças agrupadas por sala 
que frequentam cada uma das atividades.
"""
__version__ = "0.0.1"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for index, atv in atividades:
    print("{:^25}".format(f"Alunos na atividade {index}:"))
    print("-" * 40)

    atv_sala1 = []
    atv_sala2 = []

    for aluno in atv:
        if aluno in sala1:
            atv_sala1.append(aluno)
        elif aluno in sala2:
            atv_sala2.append(aluno)

    print("Sala 1: ", atv_sala1)
    print("Sala 2: ", atv_sala2)

    print()
    print("#" * 40)
