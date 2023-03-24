from math import sqrt
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

delta = B*B-4*A*C

print("Delta: ", delta)

if delta > 0:
  x1=(-B+sqrt(delta))/(2*A)
  x2=(-B-sqrt(delta))/(2*A)
  print("x1: ", x1)
  print("x2: ", x2)
else :
  print("Delta negativo: impossivel obter raízes :(")
