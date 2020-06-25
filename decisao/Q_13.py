# -*- coding: utf-8 -*-

# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor invalido.

Num = int(input("Digite um valor de 1 à 7 referente aos dias da semana: "))

if(Num == 1):
	print("Domingo")
elif(Num == 2):
	print("Segunda")
elif(Num == 3):
	print("Terça")
elif(Num == 4):
	print("Quarta")
elif(Num == 5):
	print("Quinta")
elif(Num == 6):
	print("Sexta")
elif(Num == 7):
	print("Sabado")
else:
	print("Valor Invalido")
