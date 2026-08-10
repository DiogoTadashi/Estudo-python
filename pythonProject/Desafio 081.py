'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

num = []

while True:
    num.append(int(input("Digite um valor númerico: ")))
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break
    
print(f"A quantidade de numeros digitados foram {len(num)}")

num.sort(reverse=True)
print(f"A lista de valores de forma decrescente:\n{num}")

if 5 in num:
    print(f"O valor 5 está na lista e está na posição {num.index(5) + 1}")
else:
    print("O valor 5 não está na lista")