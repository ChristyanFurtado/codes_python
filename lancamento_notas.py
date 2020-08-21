#O código irá receber os valores das notas dos 3 trimestres e dizer se o aluno passou ou não de ano.
#Fará a validação se as notas lançadas são coerentes:
#Primeiro e segundo trimestre devem receber valores de 0 a 30
#Terceiro trimestre deve receber valores entre 0 a 40

media = 60
aluno = input('Informe o nome do aluno: ')

trimestre1 = int(input('Informe a nota do primiero trimestre: '))
while trimestre1 < 0 or trimestre1 > 30:
    print('Você digitou um valor inválido para o trimestre. '
          'Digite uma nota entre 0 a 30')
    trimestre1 = int(input('Informe a nota do primiero trimestre: '))

trimestre2 = int(input('Informe a nota do segundo trimestre: '))
while trimestre2 < 0 or trimestre2 > 30:
    print('Você digitou um valor inválido para o trimestre. '
          'Digite uma nota entre 0 a 30')
    trimestre2 = int(input('Informe a nota do segundo trimestre: '))

trimestre3 = int(input('Informe a nota do terceiro trimestre: '))
while trimestre3 < 0 or trimestre3 > 40:
    print('Você digitou um valor inválido para o trimestre. '
          'Digite uma nota entre 0 a 40')
    trimestre3 = int(input('Informe a nota do terceiro trimestre: '))

nota_final = trimestre1 + trimestre2 + trimestre3

if nota_final >= media:
    print('O aluno {aluno}, ficou com a média {nf} e passou de ano!'.format(aluno=aluno, nf=nota_final))
else:
    print('O aluno {aluno}, ficou com a média {nf} e repetirá de ano!'.format(aluno=aluno, nf=nota_final))