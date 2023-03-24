"""
Verifica se um numero e par ou impar enquanto for diferente de 0
"""
num =8
while num !=0:
    num= int(input("Digite um valor: "))
    if num%2==0:
        print(num," é par")
    else:
        print(num," é impar")
