import random
import time


def jogar_jogo():
    continuar = False
    while continuar != 'nao':
        jogo = False
        lista = []
        for i in range (2, 13):
            lista.append(str(i))
        dado = random.choice(lista)
        if dado in ('7', '11'):
            print (f'Parabéns, você é um natural! você rolou {dado}, Ganhou')
        elif dado in ('2',  '3', '12'):
            print (f'Urgh, você é tirou craps! você rolou {dado}, Perdeu')
        elif dado in ('4', '5', '6', '8', '9', '10'):
            print(f"Você rolou {dado}, Portanto vai ter que rolar novamente!")
            dado_anterior = dado
            while jogo != True:
                print('Rodando novos dados...')
                time.sleep(0.5)
                dado = random.choice(lista)
                print(f'Dado novo {dado}')
                if dado_anterior == dado:
                    print (f'Parabéns, você é Ganhou! você rolou {dado}')
                    jogo = True
                elif dado == '7':
                    print (f'Que pena!você perde! você rolou {dado}')
                    jogo = True
        continuar = input("deseja continuar? ")