from datetime import date
a = float(input('Qual é o seu ano de nascimento? '))
d = date.today()
h = d.year
i = h - a
print(f'O atleta tem {i :.0f} anos')
if i <= 9:
    print('Você possui {:.0f} anos. Portanto, você é da categoria Mirim'.format(i))
elif i <= 14:
    print('Você possui {:.0f} anos. Portanto, você é da categoria Infantil'.format(i))
elif i <= 19:
    print('Você possui {:.0f} anos. Portanto, você é da categoria Junior'.format(i))
elif i <= 25:
    print('Você possui {:.0f} anos. Portanto, você é da categoria Sênior'.format(i))
elif i > 25:
    print('Você possui {:.0f} anos. Portanto, você é da categoria Master'.format(i))
