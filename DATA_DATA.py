#definição da função
def DATA_DATA(dia, mes, ano):
    if(mes==1):
        if (dia>=1) and (dia<=31):
            return True
    if(mes==2):
        if (dia>=1) and (dia<=28)and (ano%4!=0):
            return True
        if (dia>=1) and (dia<=29) and (ano%4==0):
            return True
    if(mes==3):
        if (dia>=1) and (dia<=31):
            return True
    if(mes==4):
        if (dia>=1) and (dia<=30):
            return True
    if(mes==5):
        if (dia>=1) and (dia<=31):
            return True 
    if(mes==6):
        if (dia>=1) and (dia<=30):
            return True
    if(mes==7):
        if (dia>=1) and (dia<=31):
            return True
    if(mes==8):
        if (dia>=1) and (dia<=31):
            return True
    if(mes==9):
        if (dia>=1) and (dia<=30):
            return True
    if(mes==10):
        if (dia>=1) and (dia<=31):
            return True
    if(mes==11):
        if (dia>=1) and (dia<=30):
            return True
    if(mes==12):
        if (dia>=1) and (dia<=31):
            return True

    return False

dia=int(input("Digite um Dia: "))
mes=int(input("Digite um Mes: "))
ano= int(input("Digite um Ano: "))
if (DATA_DATA(dia, mes, ano)==True):
    print("DATA VALIDA")
else:
    print("DATA INVALIDA")
