'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

num = []

while True:
    valor = int(input("Digite um valor númerico: "))
    if valor not in num:
        num.append(valor)
        print("Valor adicionado")
    else:
        print("Valor duplicado! Não será adicionado.")

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break
    
num.sort()
print(f"Os valores únicos digitados em ordem crescente são: {num}")
