# -*- coding: utf-8 -*-

"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
	1. Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
	2. Triângulo Equilátero: três lados iguais;
	3. Triângulo Isósceles: quaisquer dois lados iguais;
	4. Triângulo Escaleno: três lados diferentes;
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
    print("Não é um triangulo")
