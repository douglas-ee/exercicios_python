# -*- coding: utf-8 -*-

# Faca um programa que calcule o numero medio de alunos por Turma. Para
# isto, peca a quantidade de Turmas e a quantidade de alunos para cada
# Turma. As Turmas nao podem ter mais de 40 alunos.

Alunos_Por_Turma = []  # Lista de alunos por turma vazia a ser preenchida
Turma = 1

N_Turmas = int(input("Quantas N_Turmas? : "))  # Informando qnt de turmas

for i in range(N_Turmas):

    print("Turma ", Turma)
    alunos = int(input("Quantos Alunos tem na Turma : "))

    while alunos > 40:
        print("Turma ", Turma, " [uma Turma só pode ter 40 alunos]")
        alunos = int(input("Alunos da Turma : "))

    Alunos_Por_Turma.append(alunos)
    Turma += 1

media = sum(Alunos_Por_Turma) / len(Alunos_Por_Turma)

print("A media e igual a: ", media)
