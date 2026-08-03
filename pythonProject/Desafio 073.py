''' Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro, na ordem de colocação. Depos mostre:
A) Apenas os 5 primeiros
B) os ultimos 4 colocados
C) uma lista com os times em ordem alfabetica
D) em q posição está o time chapecoense
'''

brasileirao_2017 = (
    "Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro",
    "Flamengo", "Botafogo", "Atlético-MG", "Atlético-PR", "Bahia",
    "São Paulo", "Fluminense", "Chapecoense", "Vasco", "Sport",
    "Vitória", "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO"
)

print(f'Os primeiros 5 colocados -> {brasileirao_2017[0:5]}')
print(f'Os ultimos 4 colocados -> {brasileirao_2017[-4:]}')
print(f'Os times em ordem alfabetica -> {sorted(brasileirao_2017)}')
print(f'A posição onde está o time chapecoense -> {brasileirao_2017.index("Chapecoense")+1}')