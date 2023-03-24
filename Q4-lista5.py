peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
#FUNÇAO round() arredonda valores do tipo float
imc =round(peso/(altura**2),2)
print("IMC: ",imc)

if imc<=20:
    print("Esta abaixo do peso")
else:
    if imc >=20 and imc <=30:
        print("Esta com peso ideal")

    if imc >= 30:
        print("Esta acima do peso")
        