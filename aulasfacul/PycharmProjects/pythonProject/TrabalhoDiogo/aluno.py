from entrada import *
import json

def cadastrar_aluno(id:int):
    """
    Cadastrar um dicionário de aluno e o retorna

    Parâmetro:
        - id: inteiro com o idenficador do aluno no sistema

    Retorno:
        - aln: dicionário com as informações do aluno lidas do teclado
    """
    aln = {}
    aln['id'] = id
    aln['nome'] = input("Nome do aluno: ")
    
    #ler sexo
    while True:
        sexo = input("sexo ('M' - Masculino 'F'- Feminino 'NB' - Não-binárie) : ")
        sexo = sexo.upper() #converter para maiúsculo
        if sexo in ["M","F","NB"]:
            aln["sexo"] = sexo
            break
        else:
            print("Opção inválida! digite novamente...")
    
    aln['peso'] = ler_real("Peso (Kg): ",pos=True)
    aln['altura'] = ler_real("Altura (m):",pos=True)
    aln['mensalidade'] = ler_real("Mensalidade: ",pos=True)

    print("Cadastro de usuário lido com sucesso:\n")
    print_aluno(aln)
    #return aln
    return aln

def calcular_imc(peso:float, altura:float):
    return peso / (altura  ** 2)

def print_aluno(aln:dict):
    """
    Imprime de forma inteligível os dadosa de um dicionário de aluno
    
    Parâmetro:
        - aln: Dicionário de aluno a ser impresso
    
    """

    for chave in aln:        
        print(f"{chave.capitalize()}: {aln[chave]}")

def print_alunos(alunos:list):
    """
    Imprime o conteúdo de uma lista de alunos de forma inteligível
    
    Parâmetro:
        - alunos: Lista de dicionários de aluno
    """
    print(f"Imprimindo {len(alunos)} cadastro(s) de alunos...\n")
    
    for aln in alunos:
        print_aluno(aln)
        print("-----------------------")
        

def salvar_dados(alunos:list,id:int,imc_lista:list):
    lista = [alunos,id,imc_lista]

    try:
        with open("Alunos.json","w") as esc:
            json.dump(lista,esc,indent=4,ensure_ascii=False)
            print("Dados salvos com sucesso!")
    except:
        print("Ocorreram erros na escrita do arquivo!")


def ler_dados():
    try:
        with open("Alunos.json","r") as ler:
            lista = json.load(ler)
            print("Dados lidos com sucesso!")
            return lista
    except:
        print("Ocorreram erros na leitura do arquivos!")
    
    
def buscar_id(alunos:list):
    id_buscar = int(input("Qual id deseja buscar? "))
    id_buscar = id_buscar - 1
    print_aluno(alunos[id_buscar])
        
def filtrar_imc(imc_lista:list, lim_inf, lim_sup):
    imc_local = []
    local_contagem = 0
    for imc in imc_lista:
        if lim_inf <= imc <= lim_sup:
            local = imc_lista.index(imc)
            local += 1
            local_contagem += 1
            imc_local.append(local)
    local = ', '.join(str(item) for item in imc_local)
    if local_contagem is 0:
        print('Não tem nenhum aluno cadastrado neste tipo de IMC')
    else:
        print(f'Os IDs dos alunos desta classe respectiva de imc são {local}')
        