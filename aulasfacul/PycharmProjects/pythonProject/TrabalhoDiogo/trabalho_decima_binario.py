num = int(input('Digite o Valor Decimal que queira transformar em binário: '))
num_real = num
num_div = 1
lista = []


while num_div >= 1:
    resto = num % 2
    lista.insert(0, resto)
    num_div = num // 2
    num = num_div
binario = ''.join(str(item) for item in lista)
print(f'O número digitado foi {num_real} e o binario é {binario}')