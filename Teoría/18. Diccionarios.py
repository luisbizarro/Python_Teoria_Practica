#DICCIONARIOS
'''Son estructuras de datos que nos permiten almacenar valores de diferente tipo
(enteros, cadenas de texto, decimales, booleanos, listas, tuplas, conjuntos, diccionarios)
principal caracteristica es que los datos se almacenan asociados a 
una clave de tal forma que se crea una asociacion de tipo clave:valor para cada elemento almacenado
los elementos almacenados no estan ordenados, el orden es indiferente a la hora de almacenarlos
En un diccionario se puede añadir listas, tuplas, conjuntos, diccionarios
'''

#CREACION DE UN DICCIONARIO

#para crear un diccionario se utiliza la siguiente sintaxis
#nombre_diccionario = {clave1:valor1, clave2:valor2, clave3:valor3, clave4:valor4}

#diccionario vacio

diccionario = {}

#diccionario con elementos
#recuerda seguir la sintaxis clave:valor

diccionario = {'azul':'blue', 'rojo':'red', 'verde':'green'}

print(diccionario)

#MOSTRAR UN ELEMENTO DEL DICCIONARIO
#para mostrar un elemento del diccionario se hace de la siguiente forma
#nombre_diccionario[clave]      CON CORCHETES
#ejemplo

print(diccionario['azul'])

#AGREGAR ELEMENTOS A UN DICCIONARIO
#para agregar elementos a un diccionario se hace de la siguiente forma
#nombre_diccionario[clave] = valor
#ejemplo

diccionario_1 = {"a" : 1, "b" : 2, "luis" : 3, "FISI" : 4, "20.2" : 5}
print(diccionario_1)

diccionario_1["San Marcos"] = "UNMSM"
print(diccionario_1)
#los datos añadidos no necesariamente se agregan al final del diccionario

#TAMBIEN SE PUEDE MODIFICAR VALORES DE UN DICCIONARIO CON LA MISMA SINTAXIS
#Ejemplo

diccionario_1["b"] = "Bembos"
print(diccionario_1)

#ELIMINAR ELEMENTOS DE UN DICCIONARIO
#para eliminar elementos de un diccionario se utiliza la siguiente sintaxis
#del(nombre_diccionario[clave])
#al eliminar la clave, se elimina el valor asociado a esta
#ejemplo

diccionario_2 = {"a" : "amarillo", "b" : "blanco", "c" : "cafe", "d" : "dorado"}
print(diccionario_2)
del(diccionario_2["b"])
print(diccionario_2)


#SE PUEDE AÑADIR UNA LISTA, TUPLA O DICCINOARIO A UN DICCIONARIO
#Ejemplo

diccionario_3 = {"Luis":{"Edad":19,"Estatura":1.60},"a": "amarillo", "b" : "blanco", "c" : "cafe", "d" : "dorado"}
print(diccionario_3)