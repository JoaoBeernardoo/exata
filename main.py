from re import S
import time

def media(a=0, b=0, c=0, d=0):
    media = (a + b + c + d)/4
    print('Calculando a media...')
    time.sleep(2)
    if media > 6:
        print(f'Voce foi aprovado com a media de {media}: ')
    elif media == 6:
        print(f'Voce esta de recuperação com a media de {media}: ')
    else:
        print(f'Voce esta reprovado com a media de {media}')
    
    
    


galera = list()
dado = list()

c = 's'
while c == 's':
    dado.append(int(input('qual sua nota: ')))
    dado.append(int(input('qual sua nota: ')))
    dado.append(int(input('qual sua nota: ')))
    dado.append(int(input('qual sua nota: ')))
    galera.append(dado[:])
    dado.clear

    media(dado[0], dado[1], dado[2], dado[3])
    c = str(input('Quer continuar s/n : '))
   

print('Bem vindo ao menu')
    

      
    