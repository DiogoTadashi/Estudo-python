#62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos

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
termo = 1
while termo != 0:
    termo = int(input('Deseja mostrar mais termos, se sim quantos? '))
    for i in range(termo):
        print('{} -> '.format(new_Num), end='')
        new_Num += razao
print('Fim')