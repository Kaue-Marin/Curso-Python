def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except KeyboardInterrupt:
            print('entrada de dados interrompida pelo usuario.')
            break
        except (ValueError, TypeError):
            print(f'\033[0;31m ERRO! digite um numero valido \033[m')
            continue
        else:
            return i
def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except:
            print(f'\033[0;31m ERRO! digite um numero valido \033[m')
        else:
            return f

i = leiaint('digite um numero inteiro: ')
f = leiafloat('digite um numero real: ')
print(f'os valores digitados foram {i} e {f}')
