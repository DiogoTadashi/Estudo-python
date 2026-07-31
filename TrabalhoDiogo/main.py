from aluno import *
from entrada import *
from navegabilidade import *

x = 0
y = 1
id = 1
alunos = []
imc_lista = []

ret = ler_dados()
if ret:
    alunos = ret[0]
    id = ret[1]
    imc_lista = ret[2]
    

#carregar_arquivo()

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    #navegabilidade
    if (opc == 1):
        aln = cadastrar_aluno(id)
        alunos.append(aln)
        imc = calcular_imc(aln['peso'], aln['altura'])
        imc_lista.append(imc)
        id += 1
        
    elif (opc == 2):
        print_alunos(alunos)
    elif (opc == 3):
        buscar_id(alunos)
        #buscar id
        pass
    elif (opc == 4):
        exibir_menu_imc()
        opc_imc = ler_inteiro("Opção: ")
        if (opc_imc == 1):
            filtrar_imc(imc_lista, 0, 18.5)
        elif (opc_imc == 2):
            filtrar_imc(imc_lista, 18.5, 24.9)
        elif (opc_imc == 3):
            filtrar_imc(imc_lista, 25, 29.9)
        elif (opc_imc == 4):
            filtrar_imc(imc_lista, 30, 34.9)
        elif (opc_imc == 5):
            filtrar_imc(imc_lista, 35, 39.9)
        elif (opc_imc == 6):
            filtrar_imc(imc_lista, 40, 100)
        mostrar_aluno = input("Deseja ver a ficha de algum aluno? (S/N) ")
        if mostrar_aluno.upper() == 'N':
            pass
        else:
            continuar = "s"
            while continuar.upper() != 'N':
                buscar_id(alunos)
                continuar = input('Deseja continuar? (S/N) ')
        #filtrar por imc
        pass
    elif (opc == 5):
        salvar_dados(alunos,id,imc_lista)
        break
    else:
        print("Opção inválida!")
    limpar_tela()