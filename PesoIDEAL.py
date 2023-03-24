"""
Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1:feminino
2:masculino) de uma pessoa. Depois faça uma função chamada pesoideal que receba a altura e o
sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
a. - para homens : (72.7 * h) – 58
b. - para mulheres : (62.1 * h) – 44.7
c. Observação: Altura = h (na fórmula acima).
"""
def peso_ideal(altura, sexo):
    if (sexo ==1):
        P_ideal=(62.1 * altura)
        P_ideal = P_ideal - 44.7
    elif(sexo==2):
        P_ideal=(72.7 * altura) - 58
    else:
        print("Sexo Invalido")
        return 0
    return P_ideal

altura=float(input("Digite sua altura: "))
print("Sexo: (1)Para Mulher (2) Para Homem")
sexo=int(input("Digite o sexo: "))
print("O seu peso ideal é: ", peso_ideal(altura, sexo))
