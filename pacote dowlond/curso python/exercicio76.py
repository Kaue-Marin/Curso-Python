listagem = ('pão', 1, 'leite', 3.50, 'frango', 10.90)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='R$')
    else:
         print(f'{listagem[item]:>7.2f}')