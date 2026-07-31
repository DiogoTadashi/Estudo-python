#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
peso = float(input('Digite o peso da 1ª pessoa: '))
maior = peso
menor = peso
for i in range(2,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso é {}Kg e o menor peso é {}Kg'.format(maior, menor))