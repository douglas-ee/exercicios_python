# -*- coding: utf-8 -*-

"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contrataram para desenvolver o programa que calculará os reajustes.

	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
	critério, baseado no salário atual:

		1. salários até R$ 280,00 (incluindo) : aumento de 20%
		2. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
		3. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
		4. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
		5. o salário antes do reajuste;
		6. o percentual de aumento aplicado;
		7. o valor do aumento;
		8. o novo salário, após o aumento.
"""

Salario = float(input("Digite o Salario do colaborador: "))

Salario_A = Salario

if (Salario <= 280.0):
    Salario += Salario*0.2
if (Salario > 280.0 and Salario < 700.0):
    Salario += Salario*0.15
if (Salario >= 700.0 and Salario < 1500.0):
    Salario += Salario*0.1
if (Salario >= 1500.0):
    Salario += Salario*0.05

Aumento = Salario - Salario_A

Percentual = Aumento / Salario_A

print("Antes: {}R$, Percentual: {}%, Aumento: {}R$, Salario: {}R$".format(Salario_A, Percentual, Aumento, Salario))
