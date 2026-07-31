#63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

#n = int(input('Deseja mostrar quantos termos? '))
#cont = 3
#lista = [0, 1 , 1]
#while cont != n:
#   cont += 1
#   num = lista[-1] + lista[-2]
#   lista.append(num)
#print (lista)

n = int(input('Deseja mostrar quantos termos? '))
cont = 2
num1 = 0
num2 = 1
num3 = 0
print('{} -> {}'.format(num1, num2), end='')
while cont != n:
    num3 = num1 + num2
    print('-> {}'.format(num3), end='')
    cont += 1
    num1 = num2
    num2 = num3 
print ('-> Fim')