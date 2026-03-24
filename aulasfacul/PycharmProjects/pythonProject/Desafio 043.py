from time import sleep
print('Olá, aqui vamos calcular o seu IMC e te fornecer o seu status, apenas respondas as seguintes perguntas:')
p = float(input('Quanto você está pesando? '))
a = float(input('Quanto você possui de altura? '))
imc = float(p / (a * a))
print('='*20)
print('Calculando seu IMC')
print('='*20)
sleep(2)
print('Seu IMC é de {}'.format(imc))
if imc < 18.5:
    print('O seu status é que você está abaixo do peso')
elif 18.5 <= imc <= 25:
    print('O seu status é que você está no peso ideal')
elif 25 < imc <= 30:
    print('O seu status é que você está sobrepeso')
elif 30 < imc <= 40:
    print('Status: Obesidade')
elif imc > 40:
    print('Status: Obesidade mórbida')