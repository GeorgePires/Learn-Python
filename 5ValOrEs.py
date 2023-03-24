"""
Escrever um algoritmo que lê 5 valores, e
conta quantos destes valores são
negativos, escrevendo esta informação
"""
cont= 0
for valor in range(0,5):
    valor= int(input("Digite um valor: "))
    if valor<0:
        cont=cont +1
print("Existem ",cont,"NEGs")
