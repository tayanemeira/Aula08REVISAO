#faça um algoritmo que receba 2 notas e calcule a media
# sera aprovado se a media for a partir de 7 maior ou igual a 4 recuperação e se for menor esta reprovado
#e perguntar se deseja fazer a conta novamente
novo = "s"
while novo == "s" or novo == "S":
    nota1 = float(input("informe a primeira nota: "))
    nota2 = float(input("informe a segunda nota: "))
    media = (nota1+nota2)/2
    if media >=7:
        print ("aprovado")
    elif media >= 4:
        print ("recuperação")
    else:
        print ("reprovado")
    print (f"a sua média é {media} ")
    novo = input ("deseja fazer uma nova conta? digite s ou n: ")