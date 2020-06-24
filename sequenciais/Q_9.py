# -*- coding: utf-8 -*-

# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)

Farenheit = float(input("Digite a temperatura em Farenheit: "))

Celsius = (5 * (Farenheit - 32) / 9)

print("A conversão de Farenheit: {}, para Celsius: {}".format(Farenheit, Celsius))
