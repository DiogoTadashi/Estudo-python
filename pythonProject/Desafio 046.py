#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0 com uma pausa de 1 segundos entre eles
import time
print('Contagem regressiva para começar o estouro de fogos')
for c in range(11, 0, -1):
    print(c-1)
    time.sleep(1)
print('A queima de fogos começou! PAPAPUPUPAPULFIIILLLPUUUUUPOWPOWPOWPOWPAPAPATATATATATAFIIIIILLLFIIIIILLLLFIIIIIIILLLPOOOWWWWWW')