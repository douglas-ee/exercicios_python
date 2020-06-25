# -*- coding: utf-8 -*-

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

		1. salário bruto.
		2. quanto pagou ao INSS.
		3. quanto pagou ao sindicato.
		4. o salário líquido.

						calcule os descontos e o salário líquido, conforme a tabela abaixo:
						+ Salário Bruto : R$
						- IR (11%) : R$
						- INSS (8%) : R$
						- Sindicato ( 5%) : R$
						= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

Salario_Hora = float(input("Quanto você ganha por hora? "))
Hora_dia = int(input("Quantas horas você trabalha por dia? "))

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
