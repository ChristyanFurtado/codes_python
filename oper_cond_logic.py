v1 = int(input("Insira o primeiro valor: "))
v2 = int(input('Insira o segundo valor: '))

#Utilizando os operadores IF e ELSE

if v1 == v2:
    print('Você digitou números iguais.')
elif v1 > v2:
    print('O maior número é: {}'.format(v1))
else:
    print('O maior número é: {}'.format(v2))

v3 = int(input('Insira um terceiro valor: '))

#utilizando operador lógico AND

if v1 == v2 == v3:
    print('Você digitou números iguais.')
elif v1 > v2 and v1 > v3:
    print('O maior número é: {}'.format(v1))
elif v2 > v1 and v2 > v3:
    print('O maior número é: {}'.format(v2))
else:
    print('O maior número é: {}'.format(v3))

print('------------------------------------------------------------------------------------')

#utilizando operador lógico OR
valor1 = int(input('Entre com o valor: '))
valor2 = int(input('Entre com o valor: '))

resto1 = valor1 % 2
resto2 = valor2 % 2

if resto1 == 0 or resto2 == 0:
    print('Um dos valores digitados é par.')
else:
    print('Não foi digitado um valor par.')