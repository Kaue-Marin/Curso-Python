matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite o {l} {c} valor: '))
for l in range(0,3):
    for c in range(0,3):        
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()