# -*- coding: utf-8 -*-

# Faca um programa que leia 5 numeros e informe o maior numero.

N_1 = int(input("Digite o 1º numero: "))
N_2 = int(input("Digite o 2º numero: "))
N_3 = int(input("Digite o 3º numero: "))
N_4 = int(input("Digite o 4º numero: "))
N_5 = int(input("Digite o 5º numero: "))

if (N_1 > N_2 and N_1 > N_3 and N_1 > N_4 and N_1 > N_5):
    print("O maior numero é o 1º: ", N_1)

elif (N_2 > N_1 and N_2 > N_3 and N_2 > N_4 and N_2 > N_5):
    print("O maior numero é o 2º: ", N_2)

elif (N_3 > N_2 and N_3 > N_1 and N_3 > N_4 and N_3 > N_5):
    print("O maior numero é o 3º: ", N_3)

elif (N_4 > N_2 and N_4 > N_3 and N_4 > N_1 and N_4 > N_5):
    print("O maior numero é o 4º: ", N_4)

else:
    print("O maior numero é o 5º: ", N_5)
