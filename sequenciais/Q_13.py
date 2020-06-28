# -*- coding: utf-8 -*-

"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes formulas:
		1. Para homens: (72.7*h) - 58
		2. Para mulheres: (62.1*h) - 44.7
"""

Altura = int(input("Digite sua altura em centimetros: "))

Man = (72.7*(Altura/100)) - 58
Girl = (62.1*(Altura/100)) - 44.7

print("De acordo com a Altura {}cm, o peso ideal para homens é: {}kg, e mulheres é: {}kg.".format(
    Altura, Man, Girl))
