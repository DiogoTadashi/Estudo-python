#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Ex: Apos a sopa, A sacada da casa, A torre da derrota, O lobo ama o bolo
#Anotaram a data da da maratona

frase = str(input('Digite uma frase: ')).upper()
frase_sem_espaco = frase.replace(' ', '')
inverso = frase_sem_espaco[::-1]
print('O inverso de {} é {}'.format(frase_sem_espaco, inverso), end='')
if (frase_sem_espaco == inverso):
    print(' e a frase é um palíndromo')
else:
    print(' e a frase não é um palíndromo')