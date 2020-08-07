#Criação da lista
#Lista de um único elemento
listadecompras = ["toddy, leite, arroz, feijão, ovos, carne"]

#Imprimir a lista
print(listadecompras)

print("---------------------------------------------------------------")

#Outro formato de lista
#Lista com mais elementos
listabrasileirao = ["Flamengo", "Atlético-MG", "Grêmio", "Palmeiras", "São Paulo"]

#Imprimir segunda lista
print(listabrasileirao)

print("---------------------------------------------------------------")

#Imprimir apenas 1 elemento da lista
print(listabrasileirao[2])

print("---------------------------------------------------------------")

#Alterando elemento da lista
print(listabrasileirao)
listabrasileirao[2] = listabrasileirao[3]
listabrasileirao[3] = listabrasileirao[4]
listabrasileirao[4] = "Gremio"
print(listabrasileirao)

print("---------------------------------------------------------------")

#Deletando elemento da lista
print(listabrasileirao)
del listabrasileirao[2]
print(listabrasileirao)

print("---------------------------------------------------------------")

#Adicionando elemento na lista
print(listabrasileirao)
listabrasileirao.append("Palmeiras")
listabrasileirao.append("Santos")
print(listabrasileirao)

print("---------------------------------------------------------------")

#Listas aninhadas
lista_brasileirao_2019 = [["Flamengo-RJ", "Santos-SP", "Palmeiras-SP", "Grêmio-RS"],
                          ["Bragantino-SP", "Sport-PE", "Coritiba-PR", "Atlético-GO"],
                          ["Náutico-PE", "Sampaio Correa - MA", "Juventude-RS", "Confiança-SE"],
                          ["Brusque-SC", "Manaus-AM", "Ituano-SP", "Jacuipense-BA"]]
print(lista_brasileirao_2019)
print("---------------------------------------------------------------")
#Separando listas aninhadas
serie_a = lista_brasileirao_2019[0]
serie_b = lista_brasileirao_2019[1]
serie_c = lista_brasileirao_2019[2]
serie_d = lista_brasileirao_2019[3]
print("Os 4 primeiros colocados do Brasileirão 2019 - Série A: \n", serie_a, "\n")
print("Os 4 primeiros colocados do Brasileirão 2019 - Série B: \n", serie_b, "\n")
print("Os 4 primeiros colocados do Brasileirão 2019 - Série C: \n", serie_c, "\n")
print("Os 4 primeiros colocados do Brasileirão 2019 - Série D: \n", serie_d, "\n")

print("---------------------------------------------------------------")

campeao_serieA = serie_a[0]
campeao_serieB = serie_b[0]
campeao_serieC = serie_c[0]
campeao_serieD = serie_d[0]

print("O grande campeão da série A 2019 foi: ", campeao_serieA, "\n")
print("O grande campeão da série B 2019 foi: ", campeao_serieB, "\n")
print("O grande campeão da série C 2019 foi: ", campeao_serieC, "\n")
print("O grande campeão da série D 2019 foi: ", campeao_serieD, "\n")

print("---------------------------------------------------------------")