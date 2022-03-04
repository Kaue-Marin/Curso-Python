lista = []
c = 's'
# 1 - ler nome
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    c = str(input('quer continuar? [s/n]: '))
    if c == 'n':
        break
# 2 - ler nota
# 4 - mostrar media de cada aluno
for i, a in enumerate (lista):
    print(f'{i} {a[0]} {a[2]}')
# 5 - mostrar notas individuais
while True:
    opc = int(input('mostrar notas de qual aluno? (interrompe 999): '))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'notas de {lista[opc][0]} são {lista[opc][1]}' )