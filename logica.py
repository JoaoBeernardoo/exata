def caixa(a=0, b=0, c=0, d=0):
   soma = a + b + c + d
   print(f'O total da compra foi {soma}')


dado = list()
compra = list()
c = 'n'


while c == 'n':
   for p in range(0,4):
      dado.append(str(input('Qual nome do item: ')))
      dado.append(float(input('Qual valor do item: ')))
   
   compra.append(dado[:])
   dado.clear
   caixa(dado[1],dado[3],dado[5],dado[7])
   c = str(input('Deseja continuar? s/n'))

print('Bem vindo de volta ao menu *-*')






