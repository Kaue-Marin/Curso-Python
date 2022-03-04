def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    while inicio < fim:
        print(inicio)
        inicio += passo
    if inicio > fim:
        while inicio > fim:
            inicio -= passo
            print(inicio )
# programa principal
inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(inicio, fim, passo)