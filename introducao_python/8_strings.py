# -*- coding: utf-8 -*-

# AQUI VAMOS APRENDER UM POUCO MAIS SOBRE STRINGS E SEUS COMANDOS DE USO

A = "DOUGLAS"
B = "DOS"
C = "SANTOS"
D = "GOMES"

string_0 = "Douglas é Um Programador de Primeira!"

string_1 = string_0.lower()
string_2 = string_0.upper()
string_3 = string_0.split()
string_4 = string_0.split('o')
string_5 = string_0.find("Programador")
string_6 = string_0.replace("Primeira", "Segunda")
string_7 = len(string_0)

print(A + ' ' + B + ' ' + C + ' ' + D)  # CONCATENA STRINGS
print(string_0[string_5:])  # FAZ SLICE NA STRING
print(string_1)  # MINUSCULOS
print(string_2)  # MAIUSCULO
print(string_3)  # SUBDIVIDE EM NOVAS STRINGS BASEADO NO ' '
print(string_4)  # SUBDIVIDE EM NOVAS STRINGS BASEADO NO 'O'
print(string_5)  # BUSCA O ENDEREÇO DE ALGUMA PALAVRA OU LETRA
print(string_6)  # SUBSTITUI UMA PALAVRA POR OUTRA
print(string_7)  # ENCONTRA O TAMANHO DA STRING
