#61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

num = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a Razão da PA: '))
primeiro = num
new_Num = num + razao
cont = 1
print('{} -> '.format(primeiro), end='')
while cont != 10:
    print('{} -> '.format(new_Num), end='')
    new_Num += razao
    cont += 1
print('Fim')