maior = 0
from random import randint
import time
from operator import itemgetter
dados = {'j1': randint(1,6), 'j2': randint(1,6), 'j3': randint(1,6),
'j4': randint(1,6), 'j5': randint(1,6) }
for d,i in dados.items():
    time.sleep(1)
    print(f'joogador {d} tirou o numero {i}')
ranking = dict()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for d,i in enumerate(ranking):
    print(f'{d+1}o. {i}')