# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um valor entre 0 e 20 para receber ele por extenso: "))
    if num > 20 or num < 0:
        print("Coloque um valor novamente")
    else:
        break

print(f'Você digitou o número {extenso[num]}')
    