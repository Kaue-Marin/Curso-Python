temp = []
princ = []
mai = 0
men = 999
c = 's'
while True:
    temp.append(input('nome: '))
    temp.append(float(input('peso: ')))
    princ.append(temp[:])
    if len(temp) == 0:
        mai = temp[1]
        men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    temp.clear()
    c = input('quer continuar [s/n]: ')
    if c == 'n':
        break
print(f'o total de pessoas cadastradas foram {len(princ)}')
print(f'o maior peso foi de {mai} ', end='')
for p in princ:
    if p[1] == mai:
        print(p[0])
print(f'o menor peso foi de {men} ', end='')
for p in princ:
    if p[1] == men:
        print(p[0])
