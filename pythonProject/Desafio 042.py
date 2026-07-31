print('Olá, digite 3 números quaisquer para ver se forma um triângulo')
c1 = float(input('Digite um valor qualquer: '))
c2 = float(input('Digite um valor qualquer: '))
c3 = float(input('Digite um valor qualquer: '))
if (c1 + c2) > c3 and (c1 + c3) > c2 and (c2 + c3) > c1:
    print('Parabéns, você pode formar um triângulo')
    if c1 == c2 == c3:
        print('O seu triângulo será um triângulo Equilátero')
    elif c1 == c2 != c3 or c3 == c2 != c1 or c1 == c3 != c2:
        print('O seu triângulo será um triângulo Isósceles')
    elif c1 != c2 != c3 and c2 != c1 != c3 and c1 != c3 != c2:
        print('O seu triângulo será um triângulo Escaleno')
else:
    print('Que pena, você não pode formar um triângulo com esses valores')
