# -*- coding: utf-8 -*-

# Faca um programa que peca um numero inteiro e determine se ele eh ou nao um numero
# primo. Um numero primo eh aquele que eh divisivel somente por ele mesmo e por 1.

num = int(input("\nDigite um número: "))

if num % 2 == 0 and num != 2:
    print("não primo")
else:
    print("primo")
