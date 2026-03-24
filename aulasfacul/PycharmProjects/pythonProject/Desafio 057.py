#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = str(input('Digite qual o seu sexo M/F: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Desculpe, mas não entendi. Digite novamente o seu sexo M/F: '))
if (sexo == 'M'):
    sexo1 = 'Masculino'
elif (sexo == 'F'):
    sexo1 = 'Feminino'
print('Olá pessoa do sexo {}'.format(sexo1))