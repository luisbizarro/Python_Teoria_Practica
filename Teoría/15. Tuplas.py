# Tuplas (listas que no se pueden modificar los elementos)
# no se puede añadir ni remover elementos
#sintaxis nombredelatupla = (elemento1, elemento2, elemento3, ...)
#las tuplas consumen menos memoria que las listas y son mas rapidas que las listas

tupla_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tupla_1)

#cosas que si se pueden hacer con las tuplas
#1. acceder a los elementos de la tupla

print(tupla_1[0]) #accede al elemento 0 de la tupla

#2. acceder a un rango de elementos de la tupla

print(tupla_1[0:3]) #accede a los elementos de la posicion 0 a la 3

#3. acceder a un rango de elementos de la tupla con saltos

print(tupla_1[0:8:2]) #accede a los elementos de la posicion 0 a la 8 con saltos de 2

#4. acceder a un rango de elementos de la tupla con saltos negativos

print(tupla_1[8:0:-2]) #accede a los elementos de la posicion 8 a la 0 con saltos de 2

#5. confirmar si un elemento esta en la tupla

print(1 in tupla_1) #imprime True porque 1 esta en la tupla

#6. indicar la posicion de un elemento en la tupla

print(tupla_1.index(1)) #imprime 0 porque 1 esta en la posicion 0

#7. contar cuantas veces se repite un elemento en la tupla

print(tupla_1.count(1)) #imprime 1 porque 1 se repite 1 vez

#8. saber cuantos elementos tiene la tupla

print(len(tupla_1)) #imprime 9 porque la tupla tiene 9 elementos

#9. transformar tuplas en listas
#se usa .list(nombre de la tupla)
#ejemplo

lista_1 = list(tupla_1) #transforma la tupla en una lista

#10. transformar listas en tuplas
#se usa .tuple(nombre de la lista)
#ejemplo

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tupla_2 = tuple(lista_2) #transforma la lista en una tupla



