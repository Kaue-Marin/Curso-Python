def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31m ERRO! digite um numero valido \033[m')
        if ok:
            break

    return valor
# programa principal
n = leiaint('digite um numero: ')
print(f'você acabou de digitar o numero {n}')