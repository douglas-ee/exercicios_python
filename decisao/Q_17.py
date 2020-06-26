# -*- coding: utf-8 -*-

# Faça um Programa que peça um número correspondente a um determinado ano
# e em seguida informe se este ano é ou não bissexto.

Ano = int(input("Digite um ano: "))

if((Ano % 4) == 0):
    print("Bissexto")
else:
    print("Ano qualquer")
