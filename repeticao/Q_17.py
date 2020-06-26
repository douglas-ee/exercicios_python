# -*- coding: utf-8 -*-

# Faca um programa que calcule o fatorial de um numero inteiro fornecido pelo usuario. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite um numero: "))

for i in range(1, num, 1):
    num *= i
print(num)
