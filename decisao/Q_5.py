# -*- coding: utf-8 -*-

"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
	1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
	2. A mensagem "Reprovado", se a média for menor do que sete;
	3. A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

Nota_1 = float(input("Digite a primeira nota do aluno: "))
Nota_2 = float(input("Digite a primeira nota do aluno: "))

Media = (Nota_1 + Nota_2) / 2

if(Media == 10):
	print("Aprovado com Distinção")
else:
	if(Media >= 7.0):
		print("Aprovado")
	else:
		print("Reprovado")

	