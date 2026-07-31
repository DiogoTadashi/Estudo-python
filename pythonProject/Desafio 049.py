n = int(input("Digite o número que você queira saber a tabuada: "))
#while(n != 0):
#    cont = 0
#    while(cont <= 9):
#      cont = cont + 1
#      if((n * cont) % 2 == 0):
#          print(f"Par: {n}*{cont} = {n * cont}")
#      elif((n * cont) % 2 != 0):
#          print(f"Ímpar: {n}*{cont} = {n * cont}")
#    n = int(input())
for m in range (1, 11):
    if (n*m%2)== 0:
        print('{} x {:2} = {} - Par'.format(n, m, n*m))
    else:
        print('{} x {:2} = {} - Impar'.format(n, m, n * m))