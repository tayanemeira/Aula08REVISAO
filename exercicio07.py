#crie "um algoritmo que receba 3 numjeros e informa qual o maior entre eles
dnv = "s"
while dnv == "s" or "S":
    numero1 = int(input("informe um numero: "))
    numero2 = int(input("informe um numero: "))
    numero3 = int(input("informe um numero: "))
    if numero1 > numero2:
        if numero1 > numero3:
            print (f"o {numero1} é maior")
        else:
            print (f"o {numero3} é maior")
    elif numero2 > numero3:
            print (f"o {numero2} é maior")
    else:
            print (f"o {numero3} é maior")
    dnv = input ("gostaria de fazer a conta novamente? s/n")




