'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expressao = input("Digite uma expressão: ")

simbols = []

for simbol in expressao:
    if simbol == "(":
        simbols.append("(")
    elif simbol == ")":
        if len(simbols) > 0:
            simbols.pop()
        else:
            simbols.append(")")
            
if len(simbols) == 0:
    print("Expressão válida! Parênteses corretos.")
else:
    print("Expressão inválida! Parênteses incorretos.")