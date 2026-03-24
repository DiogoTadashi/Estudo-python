from datetime import date
a = int(input('Qual é o seu ano de nascimento? '))
data = date.today()
ah = int('{}'.format(data.year))
if ah - a < 18:
    print('Relaxa você ainda vai se alistar!')
    print('Faltam {} ano(s)'.format(abs((ah - a)-18)))
    print('Seu alistamento ocorrerá no ano {}'.format(a + 18))
elif ah - a == 18:
    print('Parabéns pelos 18 anos, você agora é um adulto e precisa se alistar!')
else:
    print('Olha só você já é de maior, já deve ter se alistado e caso não tenha corra se alistar, já está atrasado!')
    q = int(input('Digite 1 se já se alistou ou digite 2 se ainda não se alistou: '))
    if q == 1:
        print('Parabéns você já se alistou!')
    else:
        print('Caramba! Corre logo se alistar! Já faz {} ano(s) que você passou do prazo'.format((ah - a)-18))
    print('Seu alistamento foi em {}'.format(a + 18))
