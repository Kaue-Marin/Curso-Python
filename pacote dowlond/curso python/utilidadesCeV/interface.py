def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('entrada de dados interrompida pelo usuario.')
            break
        except (ValueError, TypeError):
            print(f'\033[0;31m ERRO! digite um numero valido \033[m')
            continue
        else:
            return n



def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu(lista):
    cabeçalho('menu principal'.center(37))
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[m \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32m sua opção:\033[m ')
    return opc