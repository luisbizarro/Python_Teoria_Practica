#listas

#crear una lista vacia
lista = list([])
print(lista)

#Contar la cantidad de elementos de una lista
#funcion len()
lista = [1,2,3,4,5,6,7,8,9,10]
numero_elementos = len(lista)
print(lista)
print(f"la lista tiene {numero_elementos} elementos")
print("- - - - - - - -")

#AÑADIR ELEMENTOS A LA LISTA

#Metodo append()
'''
El metodo append() añade un elemento al final de la lista
'''
#ejemplo:
lista_1 = ["luis", "juana", "maria", "pedro"]
print(lista_1)
lista_1.append("carlos")
print(lista_1)
print("- - - - - - - -")

#Metodo insert()
'''
El metodo insert() añade un elemento en la posicion que le indiquemos
'''
#ejemplo:
lista_2 = ["luis", "juana", "maria", "pedro"]
print(lista_2)
lista_2.insert(2, "carlos") #.insert(posicion, elemento)
print(lista_2)
print("- - - - - - - -")
#Metodo extend()
'''
El metodo extend() añade varios elementos al final de la lista
'''
#ejemplo:
lista_3 = ["luis", "juana", "maria", "pedro"]
print(lista_3)
lista_3.extend(["carlos", "jose", "jorge"]) #.extend([elemento1, elemento2, elemento3])
print(lista_3)
print("- - - - - - - -")


#ELIMINAR ELEMENTOS DE LA LISTA

#Metodo remove()
'''
El metodo remove() elimina el elemento que le indiquemos
'''
#ejemplo:
lista_4 = ["luis", "juana", "maria", "pedro"]
print(lista_4)
lista_4.remove("pedro") #.remove(elemento)
print(lista_4)
print("- - - - - - - -")

#Metodo pop()
'''
El metodo pop() elimina el elemento de la <posicion> que le indiquemos
'''
#ejemplo:
lista_5 = ["perro", "gato", "loro", "pez"]
print(lista_5)
lista_5.pop(2) #.pop(posicion)
print(lista_5)
print("- - - - - - - -")

#Metodo clear()
'''
Elimina todo
'''
#ejemplo:
lista_6 = ["perro", "gato", "loro", "pez", "wejnnowofw", "fw121r2"]
print(lista_6)
lista_6.clear()
print(lista_6)
print("- - - - - - - -")


#ORDEN DE UNA LISTA

#Metodo sort()
'''
Ordena la lista de menor a mayor
'''
#ejemplo:
lista_7 = [5, 2, 3, 1, 4]
print(lista_7)
lista_7.sort()
print(lista_7)

'''
Ordena la lista de mayor a menor
con el parametro reverse=True
'''

#ejemplo:
lista_8 = [5, 2, 3, 1, 4]
print(lista_8)
lista_8.sort(reverse=True)
print(lista_8)
print("- - - - - - - -")

#Metodo reverse()
'''
Invierte el orden de la lista sin ordenarla de mayor a menor o viceversa
'''
#ejemplo:
lista_9 = [5, 2, 3, 1, 4]
print(lista_9)
lista_9.reverse()
print(lista_9)
print("- - - - - - - -")


#VERIFICANDO SI UN ELEMENTO SE ENCUENTRA EN LA LISTA

#Metodo index()
'''
Devuelve la posicion del elemento que le indiquemos
'''
#ejemplo:
lista_10 = ["perro", "gato", "loro", "pez", "wejnnowofw", "fw121r2"]
print(lista_10)
posicion_arbitraria = lista_10.index("pez") #.index(elemento)
print(posicion_arbitraria)
print(f"la posición de 'pez' es {posicion_arbitraria}")
print("- - - - - - - -")



