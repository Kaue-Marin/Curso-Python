# 1 criar tupla com 20 primeiros colocados
from ast import Index


br = ('atletico mineiro', 'flamengo', 'palmeiras', 'fortaleza','corinthians', 'bragantino', 'fluminense', 'america mg', 'atletico-go', 'santos', 'ceará','internacional', 'são paulo', 'athletico pr', 'cuiába', 'juventude', 'grêmio', 'bahia', 'sport', 'chapecoense' )
# 2 mostrar na posição :5
print('os 5 primeiros são: ', br[:5])
print('-='*50)
# 3 mostrar na posição 16: 
print('os 4 ultimos são: ', br[16:])
print('-='*50)
# 4 mostrar times em ordem alfabetica(sorted)
print(sorted(br))
print('-='*50)
# 5 mostrar onde ficou a chapecoense
print('a chapecoense ficou na posiçao',br.index("chapecoense")+1)
print('-='*50)