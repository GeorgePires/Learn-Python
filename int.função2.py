def up(num1,num2,num3):
    TANK = num1
    if num2 > TANK:
        TANK = num2
    if num3 > TANK:
        TANK = num3

    return TANK

num1= int(input("Digite o 1º valor: "))
num2= int(input("Digite o 2º valor: "))
num3= int(input("Digite o 3º valor: "))

TANK = up(num1,num2,num3)

print("FULL TANK:", TANK)

