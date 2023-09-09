# Diccionario parte 2

diccionario_2 = {1:"amarillo", 2:"verde", 3:"blanco", 4:"negro", 5: "rosado"}
print(diccionario_2)

#imprimir un valor con clave dentro del diccionario
print(diccionario_2[3])

#uso del .get
#se usa para dar valores en caso no se encuentre la clave, este puede ser un mensaje.
#sintaxis nombre_del_diccionario.get(clave, "mensaje" o numero a mostrar)
#ejemplo

clave = int(input("Introduzca una clave: "))
print(diccionario_2.get(clave,"clave no encontrada"))

#COMPROBAR SI LA CLAVE SE ENCUENTRA EN EL DICCIONARIO
print(10 in diccionario_2) #imprimira False
print(1 in diccionario_2) #imprimira True

#MOSTRAR LAS CLAVES DE UN DICCIONARIO
#se usa el .keys()
#sintaxis nombre_del_diccionario.keys()
#ejemplo

print(diccionario_2.keys())
#imprimira los valores dentro de una lista

#MOSTRAR LOS VALORES DE UN DICCIONARIO
#se usa el .values
#sintaxis nombre_del_diccionario.values()
#ejemplo

print(diccionario_2.values())

#MOSTRAR CLAVES Y VALORES DE UN DICCIONARIO EN TUPLAS SEPARADAS
#se usa el .items()
#sintaxis nombre_del_diccionario.items()
#ejemplo

print(diccionario_2.items())

#CONTAR CUANTOS ELEMENTOS TIENE UN DICCIONARIO
#se usa el len()
#sintaxis len(nombre_del_diccionario)
#ejemplo

print(len(diccionario_2))

#LIMPIAR UN DICCIONARIO
#se usa el .clear()
#sintaxis nombre_del_diccionario.clear()
#ejemplo

diccionario_2.clear()
print(diccionario_2)











