# -*- coding: utf-8 -*-

# A serie de Fibonacci eh formada pela sequencia 1,1,2,3,5,8,13,21,34,55,...
# Faca um programa capaz de gerar a serie ate o n−esimo termo.

fibo = [1, 1]
i = 0
num = int(input("Entre com um número: "))

while num > len(fibo):
    fibo.append(fibo[i] + fibo[i+1])
    i += 1

print('Fibonacci(%d): %d' % (num, fibo[num-1]))

"""
n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
"""
