contador = "s"
while contador == "s" or contador == "S":
    num = int(input("diga um numero para saber se é positivo ou negativo"))
    while num ==0:
        num = int(input ("numero invalido! tente novamente"))
    if num <0:
        print ("negativo")
    else:
        print ("positivo")
        contador = input ("gostaria de fazer novamente? s/n")
