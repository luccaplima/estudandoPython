"""
DICIONARIOS

Dicionários são usados para armazenar valores de dados em chaves: valores
Um dicionario é uma coleção ordenada(a partir da versão 3.7), mutáveis e não permite duplicações

"""

#Os tipos de dados podem ser de qualquer tipo
dicionario1 = {
    "Marca": "Ford",
    "Modelo": "Fiesta",
    "Ano": 2007,
    "Elétrico": False,
    "Cores": ["Preto", "Cinza", "Vermelho"]
    }
print(dicionario1)
print(type(dicionario1))

#duplicações não são aceitas
dicionario1 = {
    "Marca": "Ford",
    "Modelo": "Fiesta",
    "Ano": 2007
    "Ano": 2011
    }

#Os itens de um dicionario podem ser referenciados pelo nome da chave

print(dicionario1["Marca"])

#Existe também um metodo get() que nos dá o mesmo resultado

print(dicionario1.get("Marca"))

#O método key() retorna uma lista com todas as chaves do dicionario

print(dicionario1.keys())

#Podemos usar a função len() para determinar quantos itens tem no dicionario

print(len(dicionario1))

#Podemos trocar os valores referenciado ao nome da chave

dicionario1["Ano"] = 2013
print(dicionario1.get("Ano"))

#Podemos adicionar itens

dicionario1["Ar-condicionado"] = True
print(dicionario1)

#Podemos fazer o mesmo utilizando o método update()

dicionario1.update({"Trava Elétrica": True})
print(dicionario1)

#Para remover itens existem vários métodos
#O método pop() remove o item referente a chave especificada

dicionario1.pop("Trava Elétrica")
print(dicionario1)

#O método popitem() remove o ultimo item inserido

dicionario1.popitem() #Nas versões anteriores a 3.7, um item aleatório era removido
print(dicionario1)

#A palavra-chave del remove o item referente a chave especificada

del dicionario1["Cores"]
print(dicionario1)

#O método clear() esvazia o dicionario

dicionario1.clear()
print(dicionario1)

#Podemos fazer um loop no dicionario usando for

dicionario1 = {
    "Marca": "Ford",
    "Modelo": "Fiesta",
    "Ano": 2007,
    "Elétrico": False,
    "Cores": ["Preto", "Cinza", "Vermelho"]
    }

for x in dicionario1:
    print(x) #imprime todos os nomes das chaves
    print(dicionario1[x]) #imprime todos os valores
    
for x in dicionario1.values(): #pode-se usar o values() para retornar os valores
    print(x)
    
for x in dicionario1.keys(): #pode-se usar o key() para retornar as chaves
    print(x)
    
#Podemos fazer um loop por ambos, chave e valor, usando o método items ()

for x, y in dicionario1.items():
  print(x, y)

#Podemos copiar um dicionario usando o método copy() ou dict()

dicionarioCopia = dicionario1.copy()
print(dicionarioCopia)

dicionarioCopia2 = dict(dicionario1)
print(dicionarioCopia2)

#Um dicionario pode conter dicionarios, isto é chamado de "nested dictionaries"

carros = {
    "carro1" : {
        "Marca": "Ford",
        "Modelo": "Fiesta",
        "Ano": 2011
        },
    "carro2" : {
        "Marca": "BMW",
        "Modelo": "320i",
        "Ano": 2018
        },
    "carro3" : {
        "Marca": "Jeep",
        "Modelo": "Renegade",
        "Ano": 2020
        }
    }

print(carros)

"""
Exercícios disponíveis em: https://www.w3schools.com/python/python_dictionaries_exercises.asp
"""
