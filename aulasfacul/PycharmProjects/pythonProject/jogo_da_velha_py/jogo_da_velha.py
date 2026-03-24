from funcoes_jogo import *

#iniciarJogo
imprimir_cabecalho()

#ler nomes
jogador = ler_nomes()

#sortear iniciante
simb = ["O","X"]
vez = sortear_jogador(jogador)

#jogar
limpar_tela()
mat = criar_matriz_jogo()

rodada = 0
result = False
while(not result):
    #ler jogada
    vez = vez%2
    print(f"{jogador[vez]}, é sua vez:")
    print_matriz(mat)
    l,c = map(int,input("Digite o valor da linha e coluna que deseja jogar separado por espaço:").split(" "))
    mat[l][c] = simb[vez]
    limpar_tela()
    result = verif_resultado(mat,jogador,simb,vez,rodada)
    vez +=1
    rodada +=1