#Bucle for
#El bucle for nos permite recorrer los elementos de una lista, tupla, cadena de texto, etc.
#sintaxis del bucle for en python es la siguiente:
# for variable in elemento a recorrer:
#     instrucciones
#ejemplo:

for i in [1,2,3,4,5]:
    print(i)
    print("hola")
    
#ejemplo 2:

coleccion = [1,"luis",2,3,4,5] #tambien puede ser una tupla, conjunto, lista.

for i in coleccion:
    print(i)

#ejejmplo 3: 
#para diccionarios

diccionario = {"luis":1,"pedro":2,"maria":3}
for i in diccionario:
    print(i) #imprime las claves
    print(diccionario[i]) #imprime los valores
    
for i in diccionario:    
    print(i, diccionario[i]) #imprime las claves y los valores
    
#tambien puedes hacerlo de la siguiente manera:
for clave, valor in diccionario.items():
    print(clave, valor)

#imprimir claves dentro de un diccionario dentro de otro diccionario
#sintaxis diccionario_1[i]["clave"]   
diccionario_1 = {"luis":{"edad":19, "altura":1.6},"pedro":{"edad":18, "altura":1.65},"maria":{"edad":19, "altura":1.61}}

for i in diccionario_1:
    print(diccionario_1[i]["edad"]) #imprime las edades
    print(diccionario_1[i]["altura"]) #imprime las alturas
    
#ejemplo 4: con cadena de texto
for i in "luis":
    print(i)
    
#USO DEL end=""
#sintaxis: print("hola", end="") #imprime hola sin salto de linea
#sintaxis 2: print("hola", end=" ") #imprime hola con un espacio en blanco
#sintaxis 3: print("hola", end="*") #imprime hola con un asterisco
#ejemplo:

for i in "luis":
    print(i, end="*") #imprime l*u*i*s*
    
    


