from random import choice
import string
def criptografia_frase():
    frase = input('Digite a frase que deseja criptografar (max:128 carac): ')
    tamanho_frase = len(frase)
    while tamanho_frase > 128:
        print('Desculpe, a frase tem mais de 128 caracteres, digite novamente!')
        frase = input('Digite a frase que deseja criptografar novamente: ')
        tamanho_frase = len(frase)
        if tamanho_frase > 128:
            print('Desculpe, a frase tem mais de 128 caracteres, digite novamente!')
    chave = input('Digite a chave da criptografia: ')
    frase_cript = ''
    chave_lista = [int(a) for a in str(chave)]
    chave_cript = chave[0::chave_lista[-1]]
    soma = 0
    for char in chave_cript:
        if char.isdigit():
            soma += int(char)
    for i in frase:
        frase_cript = frase_cript + chr(ord(i) + (soma))
    print(f'A sua frase criptografada é "{frase_cript}"')

def descriptografia():
    frase_criptografada = input('Digite a frase que deseja descriptografar: ')
    chave = input('Digite a chave da criptografia: ')
    descriptacao = ''
    chave_lista = [int(a) for a in str(chave)]
    chave_cript = chave[0::chave_lista[-1]]
    soma = 0
    for char in chave_cript:
        if char.isdigit():
            soma += int(char)
    for i in frase_criptografada:
        descriptacao = descriptacao + chr(ord(i) - (soma))
    print(f'A sua frase descriptografada é "{descriptacao}"')

def chave_cripto():
    num_lista = [1,2,3,4,5,6,7,8,9]
    gerador_chave = ''.join(choice(string.digits) for i in range(0,128))
    num = choice(num_lista)
    chave_add = gerador_chave + str(num)
    print(f'A sua chave criptografada é "{chave_add}"')
