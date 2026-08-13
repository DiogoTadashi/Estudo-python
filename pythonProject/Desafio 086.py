'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)
        
print("Matriz 3x3:")
for linha in matriz:
    for elem in linha:
        print(f"[{elem: ^5}]", end="")
    print()