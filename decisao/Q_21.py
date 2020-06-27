# -*- coding: utf-8 -*-

"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário
o valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10
reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade 
de notas existentes na máquina.

	1. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
	uma nota de 50, uma nota de 5 e uma nota de 1;
	
	2. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
	uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

Cifras_str = str(input("Digite quanto deseja sacar: "))
Cifras_QT = len(Cifras_str)
Cifras = int(Cifras_str)

if Cifras_QT == 3:
    Cem = Cifras_str[0]
    Segundo_Digito = int(Cifras_str[1])
    if(Segundo_Digito >= 5):
        Cinquenta = 1
        Dez = Segundo_Digito % 5
    else:
        Cinquenta = 0
        Dez = Segundo_Digito % 5
    Terceiro_Digito = int(Cifras_str[2])
    if(Terceiro_Digito >= 5):
        Cinco = 1
        Um = Terceiro_Digito % 5
    else:
        Cinco = 0
        Um = Terceiro_Digito % 5
    print("Notas de Cem = {}, Cinquenta = {}, Dez = {}, Cinco = {}, Um = {}. ".format(
        Cem, Cinquenta, Dez, Cinco, Um))

if Cifras_QT == 2:
    Segundo_Digito = int(Cifras_str[0])
    if(Segundo_Digito >= 5):
        Cinquenta = 1
        Dez = Segundo_Digito % 5
    else:
        Cinquenta = 0
        Dez = Segundo_Digito % 5
    Terceiro_Digito = int(Cifras_str[1])
    if(Terceiro_Digito >= 5):
        Cinco = 1
        Um = Terceiro_Digito % 5
    else:
        Cinco = 0
        Um = Terceiro_Digito % 5
    print("Notas de Cinquenta = {}, Dez = {}, Cinco = {}, Um = {}. ".format(
        Cinquenta, Dez, Cinco, Um))

if Cifras_QT == 1:
    Terceiro_Digito = int(Cifras_str[0])
    if(Terceiro_Digito >= 5):
        Cinco = 1
        Um = Terceiro_Digito % 5
    else:
        Cinco = 0
        Um = Terceiro_Digito % 5
    print("Notas de Cinco = {}, Um = {}. ".format(Cinco, Um))
