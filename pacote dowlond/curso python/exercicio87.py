spar = scol = mcoluna =  0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'escreva o numero na posição{l,c}: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print(f'a soma dos pares foram {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'a soma dos numeros da terceira coluna é {scol}')
for c in range(0,3):
    if matriz[c][1] > mcoluna:
        mcoluna =  matriz[1][c]
print(f'o maior numero da terceira coluna é {mcoluna}')