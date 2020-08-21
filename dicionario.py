#Criação de dicionário

campeoes_brasileiros = {"Palmeiras": 10, "Santos": 8, "Corinthians": 7, "Flamengo": 7, "São Paulo": 6}
print(campeoes_brasileiros)
print("------------------------------------------------------------------------------", "\n")

print("Quantos títulos brasileiros o Flamengo tem:", campeoes_brasileiros["Flamengo"])
print("---------------------------------------------", "\n")

#Funções de dicionário

print("Imprimindo chaves: ", campeoes_brasileiros.keys())
print("Imprimindo valores: ",campeoes_brasileiros.values())
print("Imprimindo itens: ", campeoes_brasileiros.items())

print("---------------------------------------------", "\n")

#Atualizando dicionários com função update

campeoes_brasileiros2 = {"Cruzeiro": 4, "Fluminense": 4, "Vasco": 4, "Internacional": 3, "Bahia": 2}

print("Primeiro dicionário: \n", campeoes_brasileiros)
print("Segundo dicionário: \n", campeoes_brasileiros2)

campeoes_brasileiros.update(campeoes_brasileiros2)

print("Dicionários unificados com a função UPDATE: \n", campeoes_brasileiros)