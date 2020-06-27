# -*- coding: utf-8 -*-

# Faca um programa que mostre todos os primos entre 1 e N sendo N um numero inteiro
# fornecido pelo usuario. O programa devera mostrar tambem o numero de divisoes que
# ele executou para encontrar os numeros primos. Serao avaliados o funcionamento, o
# estilo e o numero de testes (divisoes) executados.

lista = []  # Lista Vazia, para ser adicionada os valores que irao ser primos
divisoes = 0  # Contador de divisoes

num = int(input("Digite um numero: "))

for i in range(num + 1):

    if i % 2 == 1:
        lista.append(i)
        divisoes += 1
    else:
        divisoes += 1

print("Numeros primos: ", lista)
print("Numero de divisoes", divisoes)
