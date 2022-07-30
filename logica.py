idade = int(input("Digite uma idade: "))
nome = str(input('Digite seu nome: '))
salario = float(input('Digite seu salario: '))
sexo = str(input('Digite seu sexo: M ou F'))
estado = str(input('Digite seu estado civil: S, C, V'))


while (idade < 0 or idade > 150):
            idade = int(input("idade entre 0 ou 150 Digite uma idade: "))

while len(nome) <= 3:
        nome = str(input('Seu nome deve ter mais de 3 letras'))

while salario < 0:
        salario = float(input('Seu salario tem que ser maior que 0'))

while (sexo!='F') and (sexo!= 'M'):
        sexo = str(input('Biologicamente vc deve ser: F ou M: '))

while (estado!='S') and (estado!= 'C') and (estado != 'V'):
        estado = str(input('Esse esttado nao existe apenas: S, C, V: '))








