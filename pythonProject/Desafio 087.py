'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[], [], []]
soma = 0
soma3 = 0

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)
    
for linha in matriz:
    for elemPar in linha:
        if elemPar % 2 == 0:
            soma += elemPar
            
for linha in matriz:      
    soma3 += linha[2]

maiorV = max(matriz[1])

print("Matriz 3x3:")
for linha in matriz:
    for elem in linha:
        print(f"[{elem: ^5}]", end="")
    print()

print(f"\nA soma dos elementos pares é {soma}")

print(f"A soma dos elementos da terceira coluna é {soma3}")

print(f"O maior valor da segunda linha é {maiorV}")