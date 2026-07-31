#060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

list = []
fat = 1
num = int(input('Digite um número para calcular seu Fatorial: '))
for i in range (num, 0, -1):
    list.append(i)
    fat *= i
print(f'{num}! = {list} = {fat}')