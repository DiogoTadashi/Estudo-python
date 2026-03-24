n = int(input('Escreva qualquer número inteiro: '))
m = input('As bases de conversão: \n [1] para binário \n [2] para octal \n [3] para hexadecimal \n Escolha uma base, colocando seu número listado:')

if m == '1':
    print('O número escolhido {} em base binária é {}'.format(n, bin(n)[2:]))
elif m == '2':
    print('O número escolhido {} em base octal é {}'.format(n, oct(n)[2:]))
else:
    print('O número escolhido {} em base hexadecimal é {}'.format(n, hex(n)[2:]))

#n = int(input('Escreva qualquer número inteiro: '))
#m = input('As bases de conversão: \n [1] para binário \n [2] para octal \n [3] para hexadecimal \n Escolha uma base, colocando seu número listado:')
#if m == '1':
#    print(f'O número escolhido {n} em base binária é {format(n, "b")}')
#elif m == '2':
#    print(f'O número escolhido {n} em base octal é {format(n, "o")}')
#else:
#    print(f'O número escolhido {n} em base hexadecimal é {format(n, "x")}') EU SOU MTO GAY