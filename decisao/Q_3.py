# -*- coding: utf-8 -*-

# Faca um Programa que verifique se uma letra digitada eh "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Invalido.

Letra = input("Digite F ou M: ")

if(Letra == ('F' and 'f')):
    print("Feminino")
else:
    if(Letra == ('M' and 'm')):
        print("Masculino")
    else:
        print("Você digitou uma letra diferente de F ou M")
