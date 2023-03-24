"""
Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada
celsius para calcular e retornar o valor correspondente em graus Celsius.
a. Fórmula: C = ((F-32)/9)*5
"""

def celsius(temperatura):
    fah= ((temperatura -32)/(9)*5)
    fah= round(fah,2)
    return fah


temp=float(input("Digite uma temp em Fahrenheit :"))
print("A temperatura em Celsius é", celsius(temp))
