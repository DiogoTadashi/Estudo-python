#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
ano = int(input('Digite o seu ano de nascimento: '))
maior = 0
for i in range(2, 8):
    ano = datetime.date.today().year - ano
    if ano >= 18:
        maior += 1
        ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    else:
        ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
if maior > 1:
    print('Parabéns, no total {} pessoas são maiores de 18 anos'.format(maior))
    print('E {} pessoas são menores de idade'.format(7-maior))
elif maior == 1:
    print('Parabéns, apenas 1 pessoa é maior de 18 anos')
else:
    print('Infelizmente nenhuma pessoa é maior de 18 anos')