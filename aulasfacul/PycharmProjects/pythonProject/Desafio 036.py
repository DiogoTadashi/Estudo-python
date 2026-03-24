print('Olá, Por favor nos informe sobre as seguintes questões, para que possa saber sobre a questão do empréstimo: ')
v = float(input('Qual é o valor da casa que o você deseja? '))
s = float(input('Qual é o salário mensal que você ganha? '))
a = float(input('Em quantos anos você pretende pagar esta casa? '))
pm = v / (12*a)
ps = float(s * 0.3)
print(f'Para pegar uma casa de R${v} em {a} anos a prestação será de R${pm:.2f}')
if pm <= ps:
    print('Parabéns o seu empréstimo foi aceito')
else:
    print('Que pena! O seu empréstimo infelizmente foi negado')
