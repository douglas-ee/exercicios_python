# -*- coding: utf-8 -*-

# AQUI IREMOS ENTENDER SOBRE AS ESTRUTURAS DE CONDICAO

A = 1
B = 2
C = 1

if(A >= B):
    print('A é >= B')
else:
    print('A é < B')

if(A >= B or B < C):
    print('A >= B or B > C')
else:
    if(A == B and A == C):
        print(A == B and A == C)
    else:
        print('Nenhum condição é correta até aqui!')
