#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

nota50 = nota20 = nota10 = nota1 = 0

print("""----------------------------------\n
      Bem Vindo ao Caixa Eletrônico \n ----------------------------------""")
valor = int(input("Qual o valor desejado? R$"))
if valor >= 50:
    while valor >= 50:
        valor = valor - 50
        nota50 += 1
if valor >= 20:
    while valor >= 20:
        valor = valor - 20
        nota20 += 1
if valor >= 10:
    while valor >= 10:
        valor = valor - 10
        nota10 += 1
if valor >= 1:
    while valor >= 1:
        valor = valor - 1
        nota1 += 1
print(f"""Você sacou {nota50} cédulas de R$50
Você sacou {nota20} cédulas de R$20
Você sacou {nota10} cédulas de R$10
Você sacou {nota1} cédulas de R$1""")
print("=================================")
print("Volte sempre ao Banco DIO! Tenha um bom dia!")