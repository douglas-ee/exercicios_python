# -*- coding: utf-8 -*-

# Altere o programa anterior permitindo ao usuário informar as populacoes e as
# taxas de crescimento iniciais. Valide a entrada e permita repetir a operacao.

Ano = 0

P_A = float(input("População da cidade A: "))
Taxa_A = float(input("Taxa de crescimento da população da cidade A: "))

P_B = float(input("População da cidade B: "))
Taxa_B = float(input("Taxa de crescimento da população da cidade B: "))

while P_A < P_B:
    P_A += ((P_A*Taxa_A)/100)
    P_B += ((P_B*Taxa_B)/100)
    Ano = Ano+1

print("levará", Ano, "Anos para população da cidade A ser maior que a cidade B")
print("P_B: ", P_B, "habitantes")
print("P_A: ", P_A, "habitantes")
