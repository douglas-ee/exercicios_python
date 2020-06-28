# -*- coding: utf-8 -*-

# Faca um programa que peca uma nota, entre zero e dez. Mostre uma mensagem caso o
# valor seja invalido e continue pedindo até que o usuario informe um valor valido.

Nota = int(input("Digite uma nota entre zero e dez: "))

while (Nota > 10) or (Nota < 0):
    Nota = int(input("Digite uma nota entre zero e dez: "))

print("O valor da nota é {}".format(Nota))
