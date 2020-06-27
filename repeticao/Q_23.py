# -*- coding: utf-8 -*-

# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
# fornecido pelo usuário. O programa deverá mostrar também o número de divisões que
# ele executou para encontrar os números primos. Serão avaliados o funcionamento, o
# estilo e o número de testes (divisões) executados.

lista = []  # Lista Vazia, para ser adicionada os valrores que irão ser primos
divisoes = 0  # Contador de divisões

num = int(input("Digite um número: "))

for i in range(num + 1):

    if i % 2 == 1:
        lista.append(i)
        divisoes += 1
    else:
        divisoes += 1

print("Números primos: ", lista)
print("Número de divisões", divisoes)
