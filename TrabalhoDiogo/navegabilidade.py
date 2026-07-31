import os
import sys


def imprimir_cabecalho():
    """
    Imprime o cabeçalho do programa
    """
    cabecalho = """
****************************************************************
*                                                              *
*                         SysFitness                           *
*                                                              *
*                                     powered by:Diogo Tadashi *
****************************************************************    
"""
    print(cabecalho)

def exibir_menu():
    menu = """
 1 - Cadastrar aluno
 2 - Imprimir cadastros
 3 - Buscar aluno por id
 4 - Filtrar alunos por IMC
 5 - Salvar e sair
 -------------------------------
"""
    print(menu)

def limpar_tela():
    input("Digite 'ENTER' para continuar...")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
     
     
def exibir_menu_imc():
    menu_imc = """
 1 - Menor que 18,5	-> Magreza
 2 - 18,5 a 24,9	-> Normal
 3 - 25 a 29,9	    -> Sobrepeso
 4 - 30 a 34,9	    -> Obesidade grau I
 5 - 35 a 39,9	    -> Obesidade grau II
 6 - Maior que 40	-> Obesidade grau III
 -------------------------------
"""
    print(menu_imc)