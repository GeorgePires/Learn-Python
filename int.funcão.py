# uma função que calcule a media aritimética entre 2 valores:

#Definição da função
def media(valor1,valor2):
    med = (valor1+valor2) / 2
    return med


#Chamada da função
valor1 = int(input("Digite um valor: "))
valor2 =int(input("Digite outro valor: "))
med =media(valor1,valor2)

print(med) #ou print(media(valor1,valor2))
