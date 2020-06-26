# -*- coding: utf-8 -*-

# Altere o programa anterior para que ele aceite apenas numeros entre 0 e 1000.

lista = []
count = 0

Quantidade = int(input("Digite a quantiade de número que deseja digitar: "))

while Quantidade != count:
    numero = float(input("Digite um número: "))

    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número[erro]: "))

    lista.append(numero)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))
