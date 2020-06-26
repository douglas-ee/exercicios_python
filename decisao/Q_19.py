# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de
centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do
"e", da vírgula entre outros.
Exemplo:
	1. 326 = 3 centenas, 2 dezenas e 6 unidades, 12 = 1 dezena e 2 unidades
	2. Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

Num = str(input("Digite um Numero menor que 1000: "))

Num_Qt = len(Num)

if Num_Qt == 3:
    centena = Num[0:1]
    dezena = Num[1:2]
    unidade = Num[2:3]
    print(Num+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade + " unidades")

if Num_Qt == 2:
    dezena = Num[0:1]
    unidade = Num[1:2]
    print(Num+" = "+dezena+" dezenas, "+unidade + " unidades")

if Num_Qt == 1:
    unidade = Num[0:1]
    print(Num+" = "+unidade + " unidades")
