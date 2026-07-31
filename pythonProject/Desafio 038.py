from time import sleep
n1 = float(input('Escolha um número qualquer: '))
n2 = float(input('Escolha um número qualquer: '))
if n1 > n2:
    print('Analizando os dois números.')
    sleep(2)
    print('O primeiro valor digitado que é o número {} é maior que o segundo valor digitado {}'.format(n1, n2))
    print('Portanto, {} > {}'.format(n1, n2))
elif n1 < n2:
    print('Analizando os dois números.')
    sleep(2)
    print('O primeiro valor digitado que é o número {} é menor que o segundo valor digitado {}'.format(n1, n2))
    print('Portanto, {} < {}'.format(n1, n2))
else:
    print('Analizando os dois números.')
    sleep(2)
    print('Não existem nenhum valor maior, os dois são iguais!')
    print('Portanto, {} = {}'.format(n1, n2))
