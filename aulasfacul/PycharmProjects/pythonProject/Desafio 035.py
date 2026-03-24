print('Olá, digite 3 números quaisquer para ver se forma um triângulo')
c1 = float(input('Digite um valor qualquer: '))
c2 = float(input('Digite um valor qualquer: '))
c3 = float(input('Digite um valor qualquer: '))
if (c1 + c2) > c3 and (c1 + c3) > c2 and (c2 + c3) > c1:
    print('Parabéns, você pode formar um triângulo')
else:
    print('Que pena, você não pode formar um triângulo com esses valores')