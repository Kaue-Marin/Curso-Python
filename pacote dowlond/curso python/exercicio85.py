valores = [[],[]]
for n in range(0,7):
    v = int(input('digite um valor: '))
    if v%2==0:
        valores[0].append(v)
    elif v%2!=0:
        valores[1].append(v)
valores[0].sort()
valores[1].sort()
print(f'os valores pares foram: {valores[0]}' )
print(f'os valores impares foram: {valores[1]}' )