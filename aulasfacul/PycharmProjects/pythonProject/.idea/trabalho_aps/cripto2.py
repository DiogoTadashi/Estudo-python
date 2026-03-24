from funcao_cripto import *
escolha = False
while escolha != "4":
    escolha = input("""O que deseja fazer? (1)Criptografar (128 caracteres)
                    (2)Descriptografar 
                    (3)Criar uma chave 
                    (4)Sair: 
                    """)
    if escolha == '1':
        criptografia_frase()
    elif escolha == '2':
        descriptografia()
    elif escolha == '3':
        chave_cripto()