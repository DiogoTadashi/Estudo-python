#faça um programa que jogue par ou ímpar com o computador. O jogo só irá ser interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo
from time import sleep
from random import randint

keep = 'win'
i = 0

while True:
    print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n
    VAMOS JOGAR PAR OU ÍMPAR\n
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
    num = int(input("Diga um valor: "))
    game = ' '
    pc = randint(0, 10)
    while game not in 'PI':
        game = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    sleep(0.5)
    print("Computador escolhendo um valor.")
    print("...")
    sleep(0.5)
    print(f"Voce escolheu {num} e o computador escolheu {pc}")
    sleep(0.75)
    if game == 'P':
        if (num+pc) % 2 == 0:
            print(f"Total deu {num+pc}, portanto deu par")
            print("Você GANHOU!")
            i +=1
        else:
            print(f"Total deu {num+pc}, portanto deu ímpar")
            print("Infelizmente você PERDEU")
            break
    elif game == "I":
        if (num+pc) % 2 == 1:
            print(f"Total deu {num+pc}, portanto deu ímpar")
            print("Você GANHOU!")
            i += 1
        else:
            print(f"Total deu {num+pc}, portanto deu par")
            print("Infelizmente você PERDEU")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {i} vez(es)")