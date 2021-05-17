#estudando variaveis python

"""
python não necessita de um comando para declarar a variavel
uma variavel é criada no momento que um valor é associado a ela
uma variavel não precisa ser declarada como um tipo particular e seu tipo pode ser trocado posteriormente
O nome de uma variável em python pode ser curto (como x e y) ou pode ser mais descritivo (como idade, nome, curso)
Regras para variáveis em Python:
    1- O nome de uma variável pode começar com uma letra ou com o caractere underscore ("_")
    2- O nome de uma variável não pode começar com um número
    3- O nome de uma variável só pode conter caracteres alfa numéricos e underscores
    4- Nomes de variável são case-sensitive(idade é diferente de IDADE que é diferente de Idade)
"""

x=2136 #x é int
x=23.50 #x agora é float
y="Lucca" #y é string
z=2.50 #z é float
k=["Lucca", "João", "Matheus"] #k é list
aux=[x, y, z] #criando list com as variáveis criadas anteriormente
X = "Teste Case-Sensitive"
print(x,X) #nomes de váriaveis em python são case-sensitive

A, B, C = 'anel', 'bola', 7 #o python deixa associar valores a multiplas variáveis em apenas uma linha
print(A, B, C)

print(x)
print(y)
print(z)
print(k) 
print(aux)

"""
se é necessário especificar o tipo de dado de uma variável, isto pode ser feito com casting
"""

x1=str('Exemplo') #definindo x1 como string
x2=int(3) #definindo x2 como int
x3=float(37.5) #definindo x3 como float
x4=list(["Elemento1", "Elemento2", "Elemento3"]) #definindo x4 como lista

print(x1, x2, x3, x4)

"""
o tipo de dados de uma variavel pode ser obtido através da funçao type()
"""

print(type(x1))
print(type(x2))
print(type(x3))
print(type(x4))

"""
Variáveis que são criadas fora de uma função são consideradas váriaveis globais
e podem ser utilizadas dentro ou fora de funções
Uma variável global pode ser criada dentro de uma função utilizando a palavra-chave global
"""

var1='Python é'
var2='uma linguagem de programação interessante!'
#var1 e var2 são variáveis globais

def myfunc(): #função que utiliza as variáveis globais
    print(var1+var2)
    
myfunc() #retornar a função   

"""
Python data-types:
    texto - str
    numericos- int, float, complex
    tipos de sequencia - list, tuple, range
    tipos mapping - dict
    tipos set - set, frozenset
    tipo boolean - bool
    tipos binarios - bytes, bytearray, memoryview
"""
