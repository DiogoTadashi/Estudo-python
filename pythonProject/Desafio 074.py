import random
''' 
gerar 5 num aleatorios colocar em uma tupla 
dps listar os numeros e indicar o menor e o maior
'''

nums = tuple(random.sample(range(1, 101),5))

menor = min(nums)
maior = max(nums)

print("Os valores sorteados foram:", ", ".join(str(n) for n in nums))
print(f'O menor valor sorteado foi: {menor}')
print(f'O maior valor sorteado foi: {maior}')
