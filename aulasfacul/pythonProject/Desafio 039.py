from datetime import date
from datetime import datetime
d, m, a = int(input('Informe sua data de nascimento: ')).split()
data = date.today()
dh = int('{}'.format(data.day))
mh = int('{}'.format(data.month))
ah = int('{}'.format(data.year))
u = int(data.toordinal())
o = int(('{}-{}-{}'.format(a, m, d)))
p = int(datetime.strptime('{}'.format(o), '%Y-%m-%d'))
print('{} e {} p {}'.format(a, ah, (a-ah)))
y = int(ah-a)
if (ah - a) < 18:
    print('Relaxa você ainda vai se alistar!')
    print('Faltam {} dia(s)'.format(abs(p - u)))
elif (ah - a) == 18:
    print('Parabéns pelos 18 anos, você agora é um adulto e precisa se alistar!')
else:
    print('Olha só você já é de maior, já deve ter se alistado e caso não tenha corra se alistar, já está atrasado!')
    q = int(input('Digite 1 se já se alistou ou digite 2 se ainda não se alistou: '))
    if q == 1:
        print('Parabéns você já se alistou!')
    else:
        print('Caramba! Corre logo se alistar! Já faz {} dia(s) '.format(p - u), end=' ')
        print(' ano(s) que você passou do prazo')
