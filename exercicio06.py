#crie um codigo que leia o mês e ano que o usuario nasceu e informe a sua data
idade = int(input("informe a sua idade: "))
mes = int(input("informe o mês que você nasceu: "))
mes1 = int(input("informe o mês atual: "))
if mes >=mes1:
    conta = 2023 - idade - 1
else:
    conta = 2023 - idade
print (f"seu ano de nascimento é {conta}")