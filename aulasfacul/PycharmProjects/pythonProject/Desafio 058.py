#58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
# palpites foram necessários para vencer.
cont = False
import random
lista = []
for i in range (0,11):
    lista.append(i)
pc = random.choice(lista)
print (lista)

print('Tente acertar qual numero a maquina vai escolher de 0 a 10')
num = int(input('Digite um número: '))
while num != pc:
    cont += 1
    if num != pc:
        print('Você errou.')
        print('Não desista! Tente novamente!')
        num = int(input('Digite de 0 a 10: '))
print('Parabéns! Você acertou!')
print(f'Você tentou {cont + 1} vez(es)')
