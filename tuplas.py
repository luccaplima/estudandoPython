# -*- coding: utf-8 -*-
"""
TUPLAS

Tuplas são utilizadas para armazenar multiplos itens em uma única variável
É uma coleção ordenada, imutável e que permite valores duplicados

"""

#Criando uma tupla:

myTuple = ("Calculo", "Fisica", "Eletromag", "Calculo")
myTuple2 = ("BMW", "FORD", "FIAT", "BMW", "FORD", "FIAT")
print(myTuple,"\n",myTuple2)
print(type(myTuple), type(myTuple2))

#os itens da tupla são indexados, o primeiro item tem o index [0] e assim por diante
#quando dizemos que os itens são ordenados, isto significa que os itens tem uma ordem definida e que não será trocada
#tuplas são imutáveis, o que significa que não podemos adicionar ou remover itens depois que a tupla foi criada

"""
Para determinar quantos itens uma tupla tem, podemos usar a função len()
"""

print(len(myTuple), len(myTuple2))
print(myTuple[1])

"""
Para criar uma tupla de apenas um item, deve-se adicionar uma vírgula após o item. Sem a vírgula o Python não reconhece
como uma tupla
"""

oneTuple = ("teste",)
print(oneTuple, type(oneTuple))

#não é uma tupla
tuple = ("apple")
print(type(tuple))

"""
Os itens de uma tupla podem ser de qualquer tipo de dados
"""
tuple1 = ("1", "2", "3", "4", "5", "6")
tuple2 = ("Banana", "Maçã", "Pera", "Mamão")
tuple3 = (True, False, True)
print(tuple1, type(tuple1), "\n", tuple2, type(tuple2), "\n", tuple3, type(tuple3))

#uma tupla pode conter dados de tipos diferentes

tuple4 = ("1", "2.87", "Banana", True)
print(tuple4, type(tuple4))

#-----------------------------------------------------------------------------------------------------------
#Exercicios--->
#1) Cria uma tupla e use a sintaxe correta para imprimir o primeiro item e a quantidade de itens desta tupla.

tuplaEx1 = ("Lucca", "Mônica", "Vinicius", "Fernando")
print(tuplaEx1[0])
print(len(tuplaEx1))

#2) Use indexadores negativos para imprimir o ultimo item da tupla do exercício anterior.

print(tuplaEx1[-1])

#3) Crie uma nova tupla e use seus indexes para imprimir o teceiro, quarto e quinto item desta tupla.

tuplaEx3 = ("1", "Lucca", True, "teste", False, "Python")
print(tuplaEx3[2:5])








