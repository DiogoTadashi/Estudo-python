continuar = 's'
i = 0
while continuar in "Ss":
    num = int(input("Digite um valor qualquer para receber a tabuada: "))
    if num >= 0:
        if num == 0:
            print("O número informado é 0")
            num = int(input("Digite um número novamente: "))
    else:        
        print("O número informado é negativo")
        break
    for i in range (0,10):
        i += 1
        numTabuada = num * i
        print(f"{num} * {i} = {numTabuada}")
    continuar = input("Deseja continuar? ")