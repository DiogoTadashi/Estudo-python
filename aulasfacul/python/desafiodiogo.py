raio = float(input('Quanto o reservatório cilíndrico tem de raio? '))
altura = float(input('Quanto o reservatório cilíndrico tem de altura? '))
qnt_litros = float(input('Quantos litros a lata de tinta possui? '))
rentabilidade = float(input('Quantos m^2 rendem por litro? '))
custo = float(input('Quanto custa a lata de tinta? '))
pi = 3.14
tamanho = float((2**raio*pi)+(2*pi*raio*altura))
latas = (qnt_litros*rentabilidade) / tamanho
custo_total = custo * latas
print ("São necessários {:.2f} latas de tinta e custará {:.2f} reais para pintar os reservatórios cilíndricos".format(latas, custo_total))