# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

produtoMaior1000 = 0
valorTotal = 0
produtoBarato = 10000000000
nomeProdutoBarato = ' '

while True:
    print("""-------------------------------
    LOJA SUPER BARATÃO
-------------------------------""")
    nome = str(input("Nome do Produto: "))
    preco = float(input("preço: R$"))
    valorTotal += preco
    if preco >= 1000:
        produtoMaior1000 += 1
    if preco < produtoBarato:
        produtoBarato = preco
        nomeProdutoBarato = nome

    asw = ' '
    while asw not in 'SN':
        asw = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if asw == 'N':
        break
print("-------------- FIM DO PROGRAMA --------------")
print(f"O valor total gasto na compra foi: R${valorTotal:.2f}")
print(f"No total {produtoMaior1000} produtos custam mais de 1000 reais")
print(f"O produto mais barato foi {nomeProdutoBarato} custando {produtoBarato} reais")