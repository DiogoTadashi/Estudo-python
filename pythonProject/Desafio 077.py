''' 
tenha uma tupla com varias palavras, dps disso deve mostrar para cada palavra são suas vogais
'''

palavras = (
    "girassol",
    "montanha",
    "oceano",
    "relâmpago",
    "biblioteca",
    "viagem",
    "harmonia",
    "cristal",
    "labirinto",
    "aurora"
)
vogais = "aeiouáéíóúâêîôûãõàèìòù"

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end= '')
    for letra in palavra:
        if letra.lower() in vogais:
            print (letra, end= ' ')