n1 = float(input('Digite a nota que você tirou da nota? '))
n2 = float(input('Digite a nota que você tirou da nota? '))
m = float((n1+n2)/2)
print(f'Somando as suas duas notas que foram {n1} e {n2}, sua média ficou {m}')
if m < 5:
    print('Que pena! Você foi reprovado!')
elif m >= 5 and m <= 6.9:
    print('Você ficou de recuperação, mas você ainda tem chances! É só estudar mais e tirar uma boa nota na recuperação')
elif m >= 7:
    print('Parabéns! Você foi aprovado!')
