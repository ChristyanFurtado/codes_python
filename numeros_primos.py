#Utilizando o FOR e o RANGE para imprimir os números primeiros que existem de 0 a 100

print('Os números primos entre 1 a 100 são:')
for i in range(1, 101):
    div = 0
    for x in range(1, i + 1):
        resto = i % x
        if resto == 0:
            div+=1
    if div == 2:
        print(' O número: {} é primo.'.format(i))
