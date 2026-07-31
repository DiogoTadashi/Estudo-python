print('Olá, digite um número qualquer que te direi se é par ou ímpar')
n = float(input('número = '))
m = n % 2
if m == 0:
    print('Seu número {} é Par'.format(n))
else:
    print('Seu número {} é ímpar'.format(n))