'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

num = []
pares = []
impares = []

while True:
    num.append(int(input("Digite um valor númerico: ")))
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

for v in num:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
        
print(f"Lista completa: {num}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")