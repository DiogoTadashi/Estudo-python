#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
contador = 0
for n in range(0, 501, 3):
    if (n % 3) == 0 and not (n % 2) == 0:
        contador = contador + 1
        soma = soma + n
print('A soma de todos os números que foram {}, dá um valor total de {}'.format(contador, soma))
