import interface 

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ouve um erro na criação do arquivo!')
    else:
        print(f'arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        print('erro ao ler arquivo!')
    else:
        interface.cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
