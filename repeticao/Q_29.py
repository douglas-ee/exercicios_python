# -*- coding: utf-8 -*-

"""
  O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
  Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que
  contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a
  atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na 
  tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de
  preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
	Lojas Quase Dois - Tabela de preços
			1 		 -		 R$ 1.99
			2 		 -		 R$ 3.98
			...
			50 		 -		 R$ 99.50
"""
produtos = int(input("Digite a quantidade de produtos: "))

while produtos > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))

n_produto = 1
precos = []
for i in range(produtos):
    print("Produto N° ", n_produto)
    preco = precos.append(float(input("Digite o preco do produto: ")))
    n_produto += 1

n_produto = 1
count = 0
for j in range(produtos):
    print("Produto N° ", n_produto, "= ", precos[count])
    count += 1
    n_produto += 1