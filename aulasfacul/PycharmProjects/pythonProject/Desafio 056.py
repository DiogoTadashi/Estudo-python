#Desnvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo, qual é o nome do homem mais velho, Quantas mulheres
#têm menos de 20 anos
idade = 0
idoso = 0
menor_20 = 0
media = 0
homem_velho = 0
for i in range (1,5):
    print('-----------------')
    print('   {}ªPessoa'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')
    print('-----------------')
    media += idade
    media_total = media / 4
    if sexo == 'homem':
        if idade > idoso:
            idoso = idade
            homem_velho = nome
    if sexo == 'mulher':
        if idade < 20:
            menor_20 += 1
print('A Média de idade do grupo é {}'.format(media_total))
print('O homem mais velho é o {} e tem {} anos'.format (homem_velho, idoso))
print('Existem {} mulheres menores de 20 anos'.format(menor_20))