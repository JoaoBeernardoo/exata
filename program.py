import time

def idade(a=0, b=0, c=0):
    idadea= 2022 - a
    trab = 2022 - c
    print(f'A sua idade e {idadea}')
    print('Estamos calculando se o Sr(a) ja tem direito a aposentadoria')
    time.sleep(1)
    if b == 'M':
        if c >= 15:
            print(f' Sr tem {idadea} e mais ou 15  de contribuição por tanto pode se aposentar')
        if c < 15:
            print(f' Sr tem {idadea} porem menos que 15 anos de contribuição por tanto não pode se aposentar')  
    elif b == 'F':
        if c >= 11:
            print(f' Sra tem {idadea} e mais ou 11 anos de contribuição por tanto ira receber aposentadoria')
        if c < 11:
            print(f' sra tem {idadea} porém tem menos que 11 anos de contribuição por tanto nao tem direito a aposentadoria')
    else:
        print('Alguma informação esta incorreta favor tentar de novo')



dado = list()
dados = list()


h = 's'

while h == 's':
    dado.append(int(input('Qual o ano Sr(a) nasceu? ')))
    dado.append(str.upper((input('Qual seu sexo? F/M '))))
    dado.append(int(input('Quando foi o ano do seu primeiro trabalho? ')))
    dado.append(str(input('Qual seu nome? ')))

    dados.append(dado[:])
    dado.clear
    idade(dado[0], dado[1], dado[2])
    time.sleep(1)
    h = str.lower((input(f'Deseja continuar {dado[3]}? S/N ')))
    print('Limpando dados....')
    time.sleep(2)

time.sleep(1)
print(f'Obrigado {dado[3]} por usar nosso sistema!')






