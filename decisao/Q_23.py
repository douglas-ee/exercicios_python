# -*- coding: utf-8 -*-

# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

Num = float(input("Informe um número: "))

if Num // 1 == Num:
    print("Número inteiro")
else:
    print("Número Decimal")
