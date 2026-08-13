'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

num = [[],[]]


for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor númerico: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
        
num[0].sort()
num[1].sort()

print("\nValores pares em ordem crescente: ", num[0])
print("\nValores impares em ordem crescente: ", num[1])