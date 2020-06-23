# -*- coding: utf-8 -*-

# Faca um Programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario.

Lado = float(input("Digite o valor do comprimento lateral do quadrado: "))

Area = Lado ** 2

Area_Ao_Dobro = Area * 2

print("O valor do lado, da Area, e da Area dobrada em metros é respectivamente: {}, {}, {}".format(Lado, Area, Area_Ao_Dobro))
