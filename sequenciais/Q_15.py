# -*- coding: utf-8 -*-

"""
Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes.
Calcule e mostre o total do seu salario no referido mes, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faca um programa que nos de:

		1. salario bruto.
		2. quanto pagou ao INSS.
		3. quanto pagou ao sindicato.
		4. o salario liquido.

						calcule os descontos e o salario liquido, conforme a tabela abaixo:
						+ Salario Bruto : R$
						- IR (11%) : R$
						- INSS (8%) : R$
						- Sindicato ( 5%) : R$
						= Salario Liquido : R$

Obs.: Salario Bruto - Descontos = Salario Liquido.
"""

Salario_Hora = float(input("Quanto voce ganha por hora? "))
Hora_dia = int(input("Quantas horas voce trabalha por dia? "))

Salario_Bruto = Salario_Hora*(Hora_dia*24)
IR = (Salario_Bruto*0.11)
INSS = (Salario_Bruto*0.08)
Sindicato = (Salario_Bruto*0.05)
Descontos = IR + INSS + Sindicato
Salario_Liquido = Salario_Bruto - Descontos

print("Salario Bruto é: {}R$".format(Salario_Bruto))
print("INSS é: {}R$".format(INSS))
print("Sindicato é: {}R$".format(Sindicato))
print("Salario Liquido é: {}R$".format(Salario_Liquido))
