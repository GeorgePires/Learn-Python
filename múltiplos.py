"""
Faça um algoritmo que conte quantos valores
multiplos de 6 existem entre 1 a 100
"""
cont= 0
for valor in range(1,100+1):
    if valor %6==0:
        cont=cont+1
        

print("Existem",cont,"multiplos de 100")

