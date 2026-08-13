'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
import random

jogos = []

qtd = int(input(f"Digite o valor de quantos palpites serão gerados: "))
for i in range(qtd):
    jogo = random.sample(range(1,61),6)
    jogo.sort()
    jogos.append(jogo)

print("\nPalpites da Mega-Sena:")
for i, jogo in enumerate(jogos, start=1):
    print(f"Jogo {i}: {jogo}")