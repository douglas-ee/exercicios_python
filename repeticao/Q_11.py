# -*- coding: utf-8 -*-

# Altere o programa anterior para mostrar no final a soma dos números.

num_1 = int(input("Digite o numero inicial: "))
num_2 = int(input("Digite o numero final: "))
num_3 = 0

for i in range(num_1+1, num_2, 1):
    num_3 += i
print(num_3)


