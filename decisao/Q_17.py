# -*- coding: utf-8 -*-

# Faca um Programa que peca um numero correspondente a um determinado ano
# e em seguida informe se este ano eh ou nao bissexto.

Ano = int(input("Digite um ano: "))

if((Ano % 4) == 0):
    print("Bissexto")
else:
    print("Ano qualquer")
