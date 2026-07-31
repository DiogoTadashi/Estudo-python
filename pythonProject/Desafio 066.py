num = False
totalNum = 0
conta = False
while num != '999':
    num = int(input("Digite um numero qualquer para a soma(999 para parar): "))
    if num == 999:
        break
    totalNum += 1
    conta += num
print(f"O valor somado é de {conta} e foram um total de {totalNum} número(s) digitado(s)")