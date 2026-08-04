''' 
tenha uma tupla unica c nomes de produtos e seus respectivos preços na sequencia
no fim mostre uma listagem de preços organizando os dados em forma tabular
'''

itens =("Caneta esferográfica azul", 2.50,
    "Lápis grafite HB", 1.20,
    "Caderno universitário 200 folhas", 18.90,
    "Borracha branca", 0.80,
    "Apontador com depósito", 3.40,
    "Marca-texto amarelo", 4.50,
    "Post-it bloco 100 folhas", 7.90,
    "Grampeador pequeno", 15.00,
    "Caixa de clipes 100 unid.", 5.60,
    "Pasta plástica com elástico", 6.20)

print(f"{'Item':40} | {'Preço (R$)':>10}")
print("-"*55)

for i in range(0, len(itens), 2):
    item = itens[i]
    preco = itens[i+1]
    print(f"{item:40} | {preco:10.2f}")