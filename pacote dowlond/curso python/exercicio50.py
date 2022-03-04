from random import randint
from time import sleep

nome = str(input('qual o seu nome ? ')).strip ()
print ('Tudo bem {} vou escolher um exercicio para voce revisar'.format (nome))
exercicio=randint (1,51)
print(' Escolhendo...')
sleep (2)
print ('3')
sleep (2)
print('2')
sleep (1)
print ('achei... voce deve revisar o exercicio {} '.format (exercicio))