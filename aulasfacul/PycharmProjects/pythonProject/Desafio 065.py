#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
#valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
continuar = False
num = int(input('Digite um número: '))
continuar = input('Deseja continuar? [S/N] ')
cont = 1
total = num
maior = num
menor = num
if continuar in ('Ss'):
    while continuar not in 'Nn':
        num = int(input('Digite um número: '))
        total += num
        cont += 1
        continuar = input('Deseja continuar? [S/N] ')
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print(f'Você digitou {cont} números. A média foi {total/cont}.')
print(f'O maior número foi {maior} e o menor {menor}')