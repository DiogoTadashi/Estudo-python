print('Defina um valor a ser pago pelo produto e a maneira para que saiba o valor a ser pago:')
p = float(input('Qual é o preço normal do produto? '))
print('Defina a forma de pagamento: \n [1] - para à vista(dinheiro/cheque) \n [2] - para à vista', end=' ')
print('no cartão \n [3] - para até 2x no cartão \n [4] - para 3x ou mais no cartão')
c = int(input('Insira a condição de pagamento desejada: '))
d = (p - (p * 0.10))
ac = (p - (p * 0.05))
xc = (p + (p * 0.20))
if c == 1:
    print('O valor a ser pago por você utilizando essa maneira de pagamento é de R${}'.format(d))
elif c == 2:
    print('O valor a ser pago por você utilizando essa maneira de pagamento é de R${}'.format(ac))
elif c == 3:
    valorpar = p / 2
    print(f'Sua compra será parcelada em 2x, e cada parcela será no valor de {valorpar}')
    print(f'O valor a ser pago por você utilizando essa meneira de pagamento é de R${p}')
elif c == 4:
    parcela = int(input('Quantas parcelas vai desejar? '))
    valorparc = xc / parcela
    print('O valor a ser pago por você utilizando essa maneira de pagamento é de R${}'.format(xc))
    print(f'Sua compra será parcelada em {parcela}, e cada parcela será no valor de {valorparc}')
else:
    print('Opção inválida de pagamento, tente novamente!')