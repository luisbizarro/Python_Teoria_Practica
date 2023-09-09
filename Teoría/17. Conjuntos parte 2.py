# Conjuntos

#dato extra
'''
a = set()
a = {}

si deseas crear un conjunto con elementos ya no es necesario "a = set()"
puedes ir de frente a "a = {}" y agregar los elementos que desees

ejemplo
a = {1,2,3}
no es necesario crear un conjunto vacio si ya tiene elementos

otra cosa sería si deseas crear un conjunto vacio y luego agregar elementos
con el metodo add()
'''

#IGUALDAD DE CONJUNTOS
#para saber si 2 conjuntos son iguales se utiliza el operador ==
#ejemplo

conjunto_1 = {1,2,3}
conjunto_2 = {3,2,1}

print(conjunto_1 == conjunto_2) #imprime True porque los conjuntos son iguales

conjunto_3 = {1,2,4}

print(conjunto_1 == conjunto_3) #imprime False porque los conjuntos no son iguales

#CONTAR ELEMENTOS DE UN CONJUNTO
#para contar los elementos de un conjunto se utiliza la funcion len()
#ejemplo

conjunto_4 = {1,2,3,4,5,6,7,8,9,10}
print(len(conjunto_4)) #imprime 10 porque el conjunto tiene 10 elementos


#OPERACIONES CON CONJUNTOS

#UNION 
#para unir 2 conjuntos se utiliza el operador |
#ejemplo

a = {1,2,3}
b = {3,4,5}
c = a | b
print(c) #imprime {1,2,3,4,5}

#si te preguntas porque no se usa el operador + es porque el operador + no se puede usar con conjuntos sino en listas

#INTERSECCION
#para obtener los elementos que se repiten en 2 conjuntos se utiliza el operador &
#ejemplo

a = {1,2,3}
b = {3,4,5}
c = a & b
print(c) #imprime {3}

#DIFERENCIA
#para obtener los elementos que no se repiten en el primer conjunto del segundo conjunto se utiliza el operador -
#ejemplo

a = {1,2,3}
b = {3,4,5}
c = a - b
print(c) #imprime {1,2}

#DIFERENCIA SIMETRICA
#para obtener los elementos que no se repiten en ambos conjuntos se utiliza el operador ^
#ejemplo

a = {1,2,3}
b = {3,4,5}
c = a ^ b
print(c) #imprime {1,2,4,5}

#SUBCONJUNTO
#para saber si un conjunto es subconjunto de otro se utiliza .issubset()
#sintaxis posible_subconjunto.issubset(conjunto)
#ejemplo

a = {1,2,3}
b = {1,2,3,4,5}
print(a.issubset(b)) #se lee: ¿a es subconjunto de b? o ¿a esta en b? imprime True

#SUPERCONJUNTO
#para saber si un conjunto es superconjunto de otro se utiliza .issuperset()
#recordemos que un superconjunto es un conjunto que contiene a otro conjunto
#sintaxis posible_superconjunto.issuperset(conjunto)
#ejemplo

a = {1,2,3}
b = {1,2,3,4,5}
print(b.issuperset(a)) #se lee: ¿b es superconjunto de a? imprime True
#si no entendiste significa que ¿b contiene a a?

#DISYUNCION O CONJUNTOS DISJUNTOS
#para saber si 2 conjuntos son disjuntos se utiliza .isdisjoint()
#sintaxis conjunto_1.isdisjoint(conjunto_2)
#ejemplo

a = {1,2,3}
b = {4,5,6}
print(a.isdisjoint(b)) #se lee: ¿a es disjunto de b? imprime True

#CONJUNTOS INMUTABLES
#los conjuntos inmutables son aquellos que no se pueden modificar
#para eso se utiliza frozenset() en el conjunto
#ejemplo

a = frozenset({1,2,3})
#ahora ese conjunto no se puede modificar osea es una tupla


