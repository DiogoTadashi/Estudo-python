''' 
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

num = []

for i in range(0, 5):
    num.append(int(input("Digite um valor númerico: ")))

num.sort()
maior = max(num)
menor = min(num)
print (f"A lista em ordem crescente é {num}")
print (f"O maior número é {maior} e está na posição {num.index(maior)} e o menor é {menor} e está na posição {num.index(menor)}")