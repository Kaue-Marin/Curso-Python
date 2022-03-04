from re import L
import arquivosCev
import interface 
arq = 'curso em video.txt'
dic = {'nome':'ana', 'idade': 12, 'nome2':'pedro', 'idade': 15}
if not arquivosCev.arquivoexiste(arq):
    arquivosCev.criararquivo(arq)

while True:
    resposta = interface.menu(['ver pessoas cadastradas', 'cadastrar pessoas', 'sair do programa'])
    if resposta == 1:
        print(dic.values())
    elif resposta == 2:
        n = str(input('nome: '))
        i = int(input('idade: '))
        dic = n
        dic = i
    elif resposta == 3:
        print( 'saindo...')
        break