''' 
leia 4 valores pelo teclado, guarde em uma tupla e no fim mostre
A) qnts vzs aparece o valor 9
B) em que posição foi digitado o primeiro valor 3
C) quais foram os numeros pares
'''
valores = []
numNove = 0
num_pares = []

for i in range(4):
    num = int(input(f"Digite o {i+1}º número: "))
    valores.append(num)

tupla_valores = tuple(valores)

for i in tupla_valores:
    if i == 9:
        numNove += 1

for valor in tupla_valores:
    if valor%2 == 0:
        num_pares.append(valor)

print(f"A tupla criada foi: {tupla_valores}")
print(f"O numero nove aparece : {numNove} Vez(es)")
if 3 in tupla_valores:
    posicao_3 = tupla_valores.index(3)
    print(f"O número 3 aparece primeiro na posição {posicao_3}")
else:
    print("O número 3 não está na tupla.")
print(f"Os numeros pares foram os: {num_pares}")