# -*- coding: utf-8 -*-

# Faca um Programa que peca um número e informe se o numero eh inteiro ou decimal.
# Dica: utilize uma funcao de arredondamento.

Num = float(input("Informe um número: "))

if Num // 1 == Num:
    print("Número inteiro")
else:
    print("Número Decimal")
