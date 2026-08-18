'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

escola = []
while True:
    nome = str(input("Digite o nome da pessoa: "))
    nota1 = float(input("Digite o valor da sua primeira nota: "))
    nota2 = float(input("Digite o valor da sua segunda nota: "))
    
    escola.append([nome, nota1, nota2])
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

print("\n--- Boletim ---")
print(f"{'Nº':<4}{'Nome':<15}{'Média':>6}")
print("-" * 30)

for i, aluno in enumerate(escola, start=1):
    media = (aluno[1] + aluno[2]) / 2
    print(f"{i:<4}{aluno[0]:<15}{media:>6.1f}")
    
while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para): "))
    if opcao == 999:
        break
    if 1 <= opcao <= len(escola):
        aluno = escola[opcao - 1]
        print(f"Notas de {aluno[0]}: {aluno[1]}, {aluno[2]}")
    else:
        print("Número inválido.")