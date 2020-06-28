# -*- coding: utf-8 -*-

"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
	1. Telefonou para a vítima?
	2. Esteve no local do crime?
	3. Mora perto da vítima?
	4. Devia para a vítima?
	5. Já trabalhou com a vítima?
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente".
"""

classificado = 0

status = {0: "Inocente", 1: "Inocente",
          2: "Suspeito(a)", 3: "Cúmplice", 4: "Cúmplice", 5: "Assassino"}

perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ",
             "Devia para a vítima? ", "Já trabalhou com a vítima? "]

for i in range(len(perguntas)):
    print(perguntas[i] + " (sim ou não).")

    resposta = input("resposta: ")

    if resposta.lower() == "sim":
        classificado += 1

if classificado in status:
    print(status[classificado])
