#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
num = False
cont = 0
total = 0
print('Programa que mostra qnts numeros foram digitados e sua somas')
while num != 999:
    num = int(input('Digite números inteiros: '))
    total += num
    cont += 1
print(f'A soma total dos números foram {total-999}, foram somados {cont-1}')