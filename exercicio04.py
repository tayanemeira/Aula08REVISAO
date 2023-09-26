#crie um codigo que leia um numero diferente de zero e diga se este numero é positivo ou negativo
num = int(input("diga um numero para saber se é positivo ou negativo"))
if num ==0:
    print ("erro, tente novamente ")
elif num <0:
    print ("negativo")
else:
    print ("positivo")