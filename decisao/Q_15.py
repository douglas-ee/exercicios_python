# -*- coding: utf-8 -*-

"""
Faça um Programa que peça os 3 lados de um triangulo. O programa devera informar
se os valores podem ser um triangulo. Indique, caso os lados formem um triangulo,
se o mesmo eh: equilatero, isosceles ou escaleno.

Dicas:
	1. Tres lados formam um triangulo quando a soma de quaisquer dois lados for maior que o terceiro;
	2. Triangulo Equilatero: tres lados iguais;
	3. Triangulo Isosceles: quaisquer dois lados iguais;
	4. Triangulo Escaleno: tres lados diferentes;
"""
A = int(input("Digite o Lado 1: "))
B = int(input("Digite o Lado 2: "))
C = int(input("Digite o Lado 3: "))

if(((A + B > C) or (A + C > B) or (B + C > A)) and (A != 0 and B != 0 and C != 0)):
    if(A == B == C):
        print("Equilatero")
    elif((A == B) or (A == C) or (B == C)):
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("Nao eh um triangulo")
