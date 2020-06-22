# -*- coding: utf-8 -*-

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.

Nota = int(input("Digite uma nota entre zero e dez: "))

while (Nota > 10) or (Nota < 0):
    Nota = int(input("Digite uma nota entre zero e dez: "))

print("O valor da nota é {}".format(Nota))
