#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o
cont = 0
soma = 0
for ns in range (1, 7):
    num = int(input('Digite um valor qualquer: '.format(ns)))
    if (num % 2) == 0:
        soma = soma + num
        cont += 1
print('A soma dos {} valores informados que são pares é {}'.format(cont, soma))