#AGREGAR ELEMENTO(S) A UNA LISTA

#sea la lista de nombre lista_1

lista_1 = ["a", "b", "c", "d"]

print(lista_1)

#agregar un elemento al final de la lista
#se usa el .append((elemento))
#ejemplo

lista_1.append("e") #agregas el elemento e al final de la lista

print(lista_1)

#agregar un elemento en una posicion especifica
#se usa el .insert(indice, elemento)
#ejemplo

lista_1.insert(1, "1b") #agregas el elemento 1b en la posicion 1

print(lista_1)

#agregar varios elementos a la lista al final
#se usa el .extend([elementos])     EN OTRAS PALABRAS SE CONCATENAN LISTAS AL FINAL
#ejemplo

lista_1.extend(["f", "g", "h"]) #agregas los elementos f, g, h al final de la lista

print(lista_1)

#tambien puedes concatenar listas sumando
#ejemplo

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

print(lista_a + lista_b) #imprime [1, 2, 3, 4, 5, 6]


#BUSCAR ELEMENTO(S) DE UNA LISTA

lista_c = ["Luis", "Juan", "Pedro"]

print("Luis" in lista_c) #imprime True porque Luis esta en la lista

print("Luis" not in lista_c) #imprime False porque Luis esta en la lista

#.index nos da el indice de un elemento
#sintaxis nombredelalista.index(elemento)
#ejemplo

print(lista_c.index("Juan")) #imprime 1 porque Juan esta en la posicion 1


#CONTAR LOS VALORES REPETIDOS DE UNA LISTA

#.count nos da el numero de veces que se repite un elemento
#sintaxis nombredelalista.count(elemento)
#ejemplo

lista_d = [1,2,3,4,5,1,2,3,4,5, "luis", "luis", "juan", "juan", "juan"]

print(lista_d.count("luis")) #imprime 2 porque luis se repite 2 veces
print("la palabra Juan se repite: ", lista_d.count("juan"), " veces.") #imprime 3 porque juan se repite 3 veces


#ELIMINAR UN ELEMENTO DE UNA LISTA

#.pop elimina el elemento de una lista al final o de un indice especifico
#sintaxis nombredelalista.pop(indice)
#si no se coloca nada en el parentesis, se elimina el ultimo elemento
#ejemplo

lista_e = ["a", "b", "c", "d", "e"]

print(lista_e)

lista_e.pop() #elimina el ultimo elemento de la lista

print(lista_e) 


#ejemplo 2

lista_f = ["1a", "2b", "3c", "4d", "5e"]

print(lista_f)

lista_f.pop(0) #elimina el elemento en la posicion 0

print(lista_f)

#eliminar un elemento en especifico
#se usa el .remove(elemento)
#ejemplo

lista_g = ["aa", "bb", "cc", "dd", "ee"]

print(lista_g)

lista_g.remove("cc") #elimina el elemento cc

print(lista_g)

#eliminar todos los elementos de una lista
#se usa el .clear()
#ejemplo

lista_h = ["aaa", "bbb", "ccc", "ddd", "eee"]

print(lista_h)

lista_h.clear() #elimina todos los elementos de la lista

print(lista_h)


#LISTA VOLTEADA
#.reverse voltea la lista
#sintaxis nombredelalista.reverse()
#ejemplo

lista_i = ["aaaa", "bbbb", "cccc", "dddd", "eeee"]

print(lista_i)

lista_i.reverse() #voltea la lista

print(lista_i)


#COPIAR LISTA Y CONCATENARLA AL FINAL
lista_j = [1,2,3,4,5] * 2 #multiplica la lista por 2 y la concatena al final
print(lista_j)


#ORDENAR LOS ELEMENTOS DE UNA LISTA
#.sort ordena los elementos de una lista de menor a mayor
#sintaxis nombredelalista.sort()
#ejemplo

lista_k = [8, 2, 5, 1, 9, 3, 4, 7, -6]

print(lista_k)

lista_k.sort() #ordena la lista de menor a mayor

print(lista_k)

#si quieres ordenar los elementos de una lista de mayor a menor
#se usa el .sort(reverse=True)
#ejemplo

lista_l = [8, 2, 5, 1, 9, 3, 4, 7, -6]

print(lista_l)

lista_l.sort(reverse=True) #ordena la lista de mayor a menor

print(lista_l)




