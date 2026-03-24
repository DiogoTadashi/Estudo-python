#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
import time
termo = int(input('Digite o primeiro termo que a PA deveria começar: '))
razao = int(input('Digite a razão que a PA deveria ter: '))
print('''================================
        10 TERMOS DE UMA PA 
================================''')  
print('Calculando')
time.sleep(0.5)
print('Calculando.')
time.sleep(0.5)
print('Calculando..')
time.sleep(0.5)
print('Calculando...')
time.sleep(1)
for i in range(0,10):
    print(f' {termo} ➞ ',end='')
    termo += razao
print(' Acabou')