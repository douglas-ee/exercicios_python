# -*- coding: utf-8 -*-

"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

			                      Até 5 Kg           Acima de 5 Kg
			Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
			Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

calc_p = 0
dados_p = [("morango", 2.50, 2.20), ("maçã", 1.80, 1.50)]

while True:
    finalizar = False

    produto = input("Por favor, informe o produto desejado (Morango ou Maçã): ")

    for i in range(2):
        if produto.lower() == dados_p[i][0]:
            finalizar = True
            break
        else:
            if i == 1:
                finalizar = False
                print("Valor inválido.", produto)
    if finalizar:
        break
while True:

    peso = float(input("Por favor, informe o peso desejado:"))

    if peso > 0:
        break
    else:
        print("valor Invalido do peso.")

if (peso <= 5 and peso > 0):
    calc_p = dados_p[0][1] * peso

elif (peso > 5):
    calc_p = dados_p[0][2] * peso
    if peso > 8 or calc_p > 25:
        calc_p = calc_p - (calc_p * 0.1)

print("Valor a pagar:R$%.2f" % calc_p)
