#estudando estruturas logicas e condicionais em python

"""
o python suporta as condições de lógica usuais da matemática:
    Igual: a == b
    Diferente: a != b
    menor que: a < b
    menor ou igual a: a <= b
    maior que: a > b
    maior ou igual a: a >= b
As condições acima citadas podem ser usadas em diversas formas, porém são mais comuns em expressoes if e loops
"""

a = 150
b = 300
if b > a: #se a variavel b for maior que a variavel a, o codigo passa para a proxima linha
    print("b é maior que a!") #identação (espaço em branco) importante no código, se não houvesse iria ocorrer um erro
    
"""    
if b>a:
print("erro")
Nesse caso ocorreria um erro, pois a estrutura não está identada
"""

#----------------------------------------------------------------------------------------------------------------

A = 200
B = 200
if B > A:
    print("B é maior que A!")
elif A > B: #a palavra-chave elif é uma maneira de dizer: "se a condição anterior não for verdadeira, então tente esta condição"
    print("A é maior que B!")
elif A == B:
    print("A e B são iguais!")    
    
#---------------------------------------------------------------------------------------------------------------- 
    
x = 30
y = 800
if x > y:
    print("b é maior que a!")
elif  x == y:
    print("x e y são iguais!")
else: #a palavra-chave else processa qualquer coisa que não foi processada pelas condições precedentes
    print("y é maior que x!")

#---------------------------------------------------------------------------------------------------------------- 

x = 300
y = 250

#se só existe uma expressão a ser executada, esta pode ser colocada na mesma linha do if:
if x > y: print ("x é maior que y!") 

#se só existe uma expressão a ser executada pelo if e uma pelo else, tudo pode ser colocado na mesma linha:
print("x é maior que y!") if x > y else print ("y é maior que x!")
#---------------------------------------------------------------------------------------------------------------- 
    
x = 200
y = 10
z = 150

#o operador lógico and é usado para combinar duas condições, só passará a proxima linha se as duas condições forem satisfeitas
if x > y and z > y: 
    print("As duas condições são verdadeiras!") 

#o código só passará para a proxima linha se pelo menos uma das condições for verdadeira
if x > y or y > z:
    print("Pelo menos uma das condições é verdadeira!")






















