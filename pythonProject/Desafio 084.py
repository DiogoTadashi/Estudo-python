'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

nome_peso = []
pessoas = list()

while True:
    nome_peso.append(input(str("Digite o nome da pessoa: ")))
    nome_peso.append(int(input("Digite o peso da pessoa: ")))
    
    pessoas.append(nome_peso[:])
    nome_peso.clear()
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break
    
'''
pessoas = [
    ["Ana", 55],
    ["Carlos", 82],
    ["Beatriz", 47],
    ["João", 95],
    ["Mariana", 60],
    ["Pedro", 72],
    ["Fernanda", 49],
    ["Lucas", 88],
    ["Sofia", 53],
    ["Ricardo", 100]
]
'''

maior_peso = max(p[1] for p in pessoas)
menor_peso = min(p[1] for p in pessoas)

mais_pesados = [p[0] for p in pessoas if p[1] == maior_peso]
mais_leves = [p[0] for p in pessoas if p[1] == menor_peso]

print(f"A quantidade de pessoas cadastradas foram {len(pessoas)}")
print(f"A pessoa mais pesada tem {(maior_peso)} kgs e seu nome é {mais_pesados}")
print(f"A pessoa mais leve tem {(menor_peso)} kgs e seu nome é {mais_leves}")