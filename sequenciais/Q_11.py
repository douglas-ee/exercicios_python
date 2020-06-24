# -*- coding: utf-8 -*-

"""
 Faca um Programa que peça 2 numeros inteiros e um numero real. Calcule e mostre:
		1. o produto do dobro do primeiro com metade do segundo .
		2. a soma do triplo do primeiro com o terceiro.
		3. o terceiro elevado ao cubo.
"""

Int_1 = int(input("Digite um valor inteiro: "))
Int_2 = int(input("Digite um valor inteiro: "))
Float_1 = float(input("Digite um valor real: "))

Conta_1 = (2*Int_1)*(0.5*Int_2)
Conta_2 = (3*Int_1)+(Float_1)
Conta_3 = (Float_1 ** 3)

print("O produto do dobro de {} com metade de {} é: {}".format(Int_1, Int_2, Conta_1))
print("A soma do triplo de {} com {} é: {}".format(Int_1, Float_1, Conta_2))
print("o {} elevado ao cubo é: {}".format(Float_1, Conta_3))
