a = int(input('Insira o primeiro número para as operações: '))
b = int(input("Insira o segundo número para as operações: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = int(a / b)
resto = a % b

resultados = ("Esses são os resultados das operações com os números inseridos: "
      "\n Soma: {soma}"
      "\n Subtração: {sub}"
      "\n Multiplicação: {multi}"
      "\n Divisão: {div}"
      "\n Resto da divisão: {resto}" .format(soma=soma,
                                             sub=subtracao,
                                             multi=multiplicacao,
                                             div=divisao,
                                             resto=resto))

print(resultados)
