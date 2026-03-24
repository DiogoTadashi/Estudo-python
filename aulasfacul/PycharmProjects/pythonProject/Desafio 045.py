import random
from time import sleep
print('Olá gamigo, vamos jogar um jokenpo? O famoso pedra, papel e tesoura?')
print('Prometo que não vou roubar haha')
m = random.randrange(1, 4)
print('Vamos começar?')
print('Já vai pensando no que vai escolher haha, eu já escolhi o meu!')
e = str(input('Escreva aqui a sua escolha, não vou ver: '))
print('Ok, agora que escolheu vamos jogar juntos! No 3')
print('1')
sleep(0.7)
print('2')
sleep(0.7)
print('3, Já!!')
if m == 1:
    print('A minha escolha foi {}{}{}!'.format('\033[4;31m', 'Pedra', '\033[m'))
elif m == 2:
    print('A minha escolha foi {}{}{}!'.format('\033[4;34m', 'Papel', '\033[m'))
elif m == 3:
    print('A minha escolha foi {}{}{}!'.format('\033[4;33m', 'Tesoura', '\033[m'))
sleep(0.5)
if e == 'pedra':
    print('A sua escolha foi {}{}{}!'.format('\033[4;31m', 'Pedra', '\033[m'))
elif e == 'papel':
    print('A sua escolha foi {}{}{}!'.format('\033[4;34m', 'Papel', '\033[m'))
elif e == 'tesoura':
    print('A sua escolha foi {}{}{}!'.format('\033[4;33m', 'Tesoura', '\033[m'))
sleep(0.4)
if e == 'pedra' and m == 1:
    print('Ah! Olha só, Mentes brilhantes pensam igual, a gente empatou!')
elif e == 'pedra' and m == 2:
    print('Olha só! eu ganhei haha, sem nenhum tipo de trapaça!')
elif e == 'pedra' and m == 3:
    print('Ah não! Eu perdi! você deve ter trapaceado!')
elif e == 'papel' and m == 1:
    print('Ah não! Eu perdi! você deve ter trapaceado!')
elif e == 'papel' and m == 2:
    print('Ah! Olha só, Mentes brilhantes pensam igual, a gente empatou!')
elif e == 'papel' and m == 3:
    print('Olha só! eu ganhei haha, sem nenhum tipo de trapaça!')
elif e == 'tesoura' and m == 1:
    print('Olha só! eu ganhei haha, sem nenhum tipo de trapaça!')
elif e == 'tesoura' and m == 2:
    print('Ah não! Eu perdi! você deve ter trapaceado!')
elif e == 'tesoura' and m == 3:
    print('Ah! Olha só, Mentes brilhantes pensam igual, a gente empatou!')
