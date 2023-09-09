#METODOS DICCIONARIOS

'''
keys() -> Devuelve una lista con las claves del diccionario
get() -> Devuelve el valor de la clave especificada
clear() -> Remueve todos los elementos del diccionario
pop() -> Remueve el elemento con la clave especificada
items() -> Devuelve una lista que contiene una tupla para cada par clave-valor

'''

diccionario = {
    "nombre" : "Luis",
    "apellido" : "Bizarro",
    "edad" : 19,
    "carrera" : "Ingenieria de software",
    "ciclo" : "2"
}
#keys
claves = diccionario.keys()
print(claves)

#OBTENER EL VALOR

#get() -> devuelve el valor de la clave especificada, y 
#si no existe la clave devuelve un valor por defecto (NONE)
#y el programa continua funcionando
valor = diccionario.get("nombre")
print(valor)

#diccionario[clave] -> devuelve el valor de la clave especificada
#y si no existe la clave devuelve un ERROR.
#y el programa se detiene
valor = diccionario["nombre"]
print(valor)

#diccionario como lista (no recomendado)
diccionario_lista = {
    1 : "Luis",
    2 : "Bizarro",
    3 : 19,
    4 : "Ingenieria de software",
    5 : "2"
}

#CLEAR  (ELIMINA TODOS LOS ELEMENTOS DEL DICCIONARIO)
diccionario_lista.clear()
print(diccionario_lista)

#POP (ELIMINA EL ELEMENTO CON LA CLAVE ESPECIFICADA)
diccionario_2 = {
    "alumno" : "Luis",
    "apellido" : "Bizarro",
    "edad" : 19,
    "carrera" : "Ingenieria de software",
    "ciclo" : "2"
}    
print(diccionario_2)
diccionario_2.pop("alumno") #SI NO EXISTE LA CLAVE, DEVUELVE UN ERROR
print(diccionario_2)


#PARA PODER ITERAR EL DICCIONARIO
#items() -> devuelve una lista que contiene una tupla para cada par clave-valor
diccionario_3 = {
    "alumno" : "Luis",
    "apellido" : "Bizarro",
    "edad" : 19,
}
print(diccionario_3.items())



