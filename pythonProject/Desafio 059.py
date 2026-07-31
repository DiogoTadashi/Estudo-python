#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
opcao = False

while opcao != 5:
    opcao = int(input('''Digite qual operação deseja
                [ 1 ] somar
                [ 2 ] multiplicar
                [ 3 ] maior
                [ 4 ] novos números
                [ 5 ] sair do programa
                Qual operação: '''))
    if opcao == 1:
        print(f'A soma dos números são {num1 + num2}')
    elif opcao == 2:
        print(f'A multiplicação dos números são {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior dos números são {num1}')
        else:
            print(f'O maior número é o {num2}')
    elif opcao == 4:
        print('Você escolheu mudar os números, digite os novos números')
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um número: '))
print('Você escolheu sair.')
