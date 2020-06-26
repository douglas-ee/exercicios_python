# -*- coding: utf-8 -*-

"""
Faca um Programa para uma loja de tintas. O programa devera pedir o tamanho em metros quadrados da
area a ser pintada. Considere que a cobertura da tinta eh de 1 litro para cada 6 metros quadrados e
que a tinta eh vendida em latas de 18 litros, que custam R$ 80,00 ou em galoes de 3,6 litros, que
custam R$ 25,00.

Informe ao usuario as quantidades de tinta a serem compradas e os respectivos preços em 3 situacoes:
	1. comprar apenas latas de 18 litros;
	2. comprar apenas galões de 3,6 litros;
	3. misturar latas e galoes, de forma que o preco seja o menor. Acrescente 10% de folga e sempre
	   arredonde os valores para cima, isto eh, considere latas cheias.
"""

tamanho = float(input("Digite o Tamanho em M² a ser pintado: "))
Cobertura = tamanho / 6

print("Você precisa comprar {}L de tinta: ".format(Cobertura))

print("Lata de 18L custa 80R$")
print("Galao de 3,6L custa 25R$")
print("Misturado 10% de desconto")
