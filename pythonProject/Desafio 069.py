#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
continuar = 's'
i = 0
personMore18 = 0
men = 0
womenLess20 = 0

print("Bem vindo ao programa de cadastramento de clientes, Vamos começar?")
while continuar in "Ss":
    print("""------------------------------\n
    CADASTRE UMA PESSOA\n
------------------------------""")
    age = int(input("Idade: "))
    sex = " "
    while sex not in 'MF':
        sex = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if age >= 18:
        personMore18 += 1
    if sex == 'M':
        men += 1
    if sex == 'F' and age < 20:
        womenLess20 += 1
    continuar = input("Deseja continuar? ")

print(f"Você cadastrou {personMore18} pessoas maiores de 18 anos")
print(f"Você cadastrou {men} homens no total")
print(f"Você cadastrou {womenLess20} mulheres com menos de 20 anos")