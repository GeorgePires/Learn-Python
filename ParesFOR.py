""" 4 – Crie e aplique uma função que receba um número inteiro e imprima
todos os pares de 0 até ele.
"""

def pares(num):
    for i in range(0,num+1):
        if i%2==0:
            print(i)

num=int(input("Digite um numero int: "))
pares(num)
