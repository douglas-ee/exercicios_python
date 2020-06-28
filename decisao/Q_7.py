# -*- coding: utf-8 -*-

# Faca um Programa que leia tres números e mostre o maior e o menor deles.

Num_1 = int(input("Digite o primeiro numero: "))
Num_2 = int(input("Digite o primeiro numero: "))
Num_3 = int(input("Digite o primeiro numero: "))

# MAIOR NUMERO

if((Num_1 > Num_2) and (Num_1 > Num_3)):
    print(Num_1)
else:
    if((Num_2 > Num_1) and (Num_2 > Num_3)):
        print(Num_2)
    else:
        print(Num_3)

# MENOR NUMERO

if((Num_1 < Num_2) and (Num_1 < Num_3)):
    print(Num_1)
else:
    if((Num_2 < Num_1) and (Num_2 < Num_3)):
        print(Num_2)
    else:
        print(Num_3)
