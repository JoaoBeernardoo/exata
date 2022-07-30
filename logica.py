c = 0
media = 0
numeros= []
soma = 0
while c < 5:
        numeros.append(float(input("Digite um numero: ")))
        c = c + 1
cont = 1
while cont  < len(numeros):
        if numeros[cont] != 0:
           soma = soma+ numeros[cont]
        cont = cont + 1


media = soma / 5

print(f'{soma}')
print(f'a sua media e {media}')

        









