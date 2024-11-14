import random
matriz=[]

for a in range(4):
    linha=[]
    for b in range(4):
        numero_aleatorio = random.randint(1, 99)
        linha.append(numero_aleatorio)
    matriz.append(linha)

print('-- Matriz --')
for i in matriz:
    for elemento in i:
        print(f'{elem  
    print('')
print()

valor = 0 
for a in range(4):
    if matriz[a][2] > valor:
        print(f'o maior valor da 3° coluna é: {valor}')

soma = 0

for a in range (4):
    soma+= matriz[a][a]
print(f'A soma da diagonal principal é:  {soma} ')