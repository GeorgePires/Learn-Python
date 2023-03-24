"""
Faça um algoritmo que, dado um valor
entre 0 a 10 definido pelo computador,
o usuário dê o seu palpite até acertar o
valor que o computador “sorteou”.
"""
from random import randint
a= randint(0,10)
i= 1000
while(i !=a):
    i= int(input("Digite um valor: "))
    if(i<a):
        print("Esta baixo")
    if(i>a):
        print("Esta alto")
    if(i==a):
        print("========*PARABENS*========")
        print("========VOCE ACERTOU======")
