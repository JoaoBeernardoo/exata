n1 = float(input('Digite sua nota: '))

n2= float(input('Digite sua nota: '))

media=(n1+n2)/2

if media > 6:
    print(f'Aprovado sua media é {media}')

elif media == 6:
    print(f'Recuperação sua media é {media}')

else:
    print(f'Reprovado sua media é {media}')



