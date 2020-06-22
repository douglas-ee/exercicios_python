# -*- coding: utf-8 -*-

"""
Faça um programa que leia e valide as seguintes informações:
	1.Nome: maior que 3 caracteres;
	2.Idade: entre 0 e 150;
	3.Salário: maior que zero;
	4.Sexo: 'f' ou 'm';
	5.Estado Civil: 's', 'c', 'v', 'd';
"""

Nome = str(input("informe um nome: "))
while (len(Nome) <= 3):
    Nome = str(input("informe um nome: "))

Idade = int(input("informe sua Idade: "))
while (Idade > 150 or Idade < 0):
    Idade = int(input("informe sua Idade: "))

Salario = float(input("informe seu Salario: "))
while (Salario < 0):
    Salario = float(input("informe seu Salario: "))

Sexo = str(input("informe seu Sexo: "))
while Sexo.lower() != 'f' and Sexo.lower() != 'm':
    Sexo = str(input("informe seu Sexo: "))

Estado_Civil = str(input("informe seu Estado Civil: "))
while Estado_Civil.lower() != "s" and Estado_Civil.lower() != "c" and Estado_Civil.lower() != "v" and Estado_Civil.lower() != "d":
    Estado_Civil = str(input("informe seu Estado Civil: "))


print("Meu nome é: " + Nome)
print("Minha Idade é: " + str(Idade))
print("Meu Salario é: " + str(Salario))
print("Meu Sexo é: " + Sexo)
print("Meu Estado Civil é: " + Estado_Civil)
