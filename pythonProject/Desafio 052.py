#Desenvolva um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número: '))
divisivel = 0
vermelho = '\033[31m'
verde = '\033[32m'
for i in range(1, num+1):
    conta = num % i
    if (conta == 0):
        print(f'{vermelho}', end='')
        divisivel += 1
    else:
        print(f'{verde}', end='')
    print('{} \033[0;0m'.format(i), end='')
if (divisivel == 2):
    print("""\nO número {} foi divisível {} vezes, além do 1 e por si próprio
E por isso ele É PRIMO""".format(num, (divisivel-2)))
else:
    print("""\nO número {} foi divisível {} vezes, {} além do 1 e por si próprio
E por isso ele NÃO É PRIMO""".format(num, divisivel, (divisivel-2)))