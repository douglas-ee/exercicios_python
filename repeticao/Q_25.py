# -*- coding: utf-8 -*-

# Faca um programa que peca para n pessoas a sua idade, ao final o programa devera
# verificar se a media de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e entao, dizer se a turma eh jovem, adulta ou idosa, conforme a media calculada.

lista = []  # Lista vazia à ser preenchida

pessoas = int(input("Digite o número de pessoas que ira digitar a idade: "))

for i in range(pessoas):  # FOR que ira percorrer as N-Pessoas
    # Colocando idade em cada umas das N-Pessoas
    idade = lista.append(int(input("Digite a idade: ")))

Media = sum(lista) / len(lista)

if Media < 25:
    print("jovem")
elif Media >= 25 and Media < 60:
    print("adulto")
else:
    print("idosa")

print(lista)
