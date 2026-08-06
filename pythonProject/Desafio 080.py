'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

num = []

for i in range(0, 5):
    valor = int(input("Digite um valor númerico: "))
    
    if i == 0 or valor > num[-1]:
        num.append(valor)
    else:
        pos = 0
        while pos < len(num):
            if valor <= num[pos]:
                num.insert(pos, valor)
                break
            pos += 1

print(f"Os valores digitados foram: {num}")