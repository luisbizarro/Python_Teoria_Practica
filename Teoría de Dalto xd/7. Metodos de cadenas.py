#METODOS DE CADENAS

#METODOS QUE DEVUELVEN UN VALOR

#Metodo upper() y lower()
#El metodo upper() convierte a mayusculas y el metodo lower() convierte a minusculas
#Ejemplo:
cadena = "Hola Mundo"
print(cadena.upper())
print(cadena.lower())

#Metodo capitalize()
#El metodo capitalize() convierte la primera letra de la cadena en mayuscula
#Ejemplo:
cadena = "hola mundo"
print(cadena.capitalize())

#METODOS QUE BUSCAN UNA SUBCADENA EN UNA CADENA

#Metodo find()
'''
El metodo find() busca una subcadena dentro de otra cadena, devolviendo la posicion
en la que se encuentra la subcadena. Si no la encuentra devuelve -1
'''
#ejemplo:
cadena = "Hola Mundo"
busqueda_find = cadena.find("Mundo") #Devuelve 5 porque la posicion de la M es 5 en la cadena "Hola Mundo" 
print(busqueda_find)

#Metodo index()
'''
El metodo index() busca una subcadena dentro de otra cadena, devolviendo la posicion
en la que se encuentra la subcadena. Si no la encuentra devuelve un error
'''
#ejemplo:
cadena = "Hola Mundo"
busqueda_index = cadena.index("Mundo") #Devuelve 5 porque la posicion de la M es 5 en la cadena "Hola Mundo"
print(busqueda_index)
busqueda_index1 = cadena.index("o")
print(busqueda_index1)


#METODOS QUE COMPRUEBAN EL TIPO DE CARACTERES DE LA CADENA

#Metodo isnumeric()
'''
El metodo isnumeric() comprueba si la cadena esta formada solo por caracteres numericos
'''
#ejemplo:
cadena = "123456"
print(cadena.isnumeric()) #Devuelve True porque la cadena esta formada solo por caracteres numericos

#Metodo isalpha()
'''
El metodo isalpha() comprueba si la cadena esta formada solo por caracteres alfabeticos
'''
#ejemplo:
cadena = "Hola Mundo"
print(cadena.isalpha()) #Devuelve False porque la cadena no esta formada solo por caracteres alfabeticos


#METODOS QUE CUENTAN

#Metodo count()
'''
El metodo count() cuenta el numero de veces que aparece una subcadena dentro de otra cadena
'''
#ejemplo:
cadena = "Hola Mundo"
contador = cadena.count("o") #Devuelve 2 porque la letra "o" aparece 2 veces en la cadena "Hola Mundo"
print(contador)

#Metodo len()
'''
El metodo len() devuelve la longitud de la cadena, es decir, el numero de caracteres que contiene
'''
#ejemplo:
cadena = "Hola Mundo"
longitud = len(cadena) #Devuelve 10 porque la cadena "Hola Mundo" tiene 10 caracteres
print(longitud)


#METODOS QUE COMPRUEBAN EL CONTENIDO DE LA CADENA

#Metodo startswith()
'''
El metodo startswith() comprueba si la cadena comienza con la subcadena indicada
'''
#ejemplo:
cadena = "Hola Mundo"
comieza_con = cadena.startswith("Ho")
print(comieza_con) #Devuelve True porque la cadena comienza con "Ho"

#Metodo endswith()
'''
El metodo endswith() comprueba si la cadena termina con la subcadena indicada
'''
#ejemplo:
cadena = "Hola Mundo"
termina_con = cadena.endswith("do")
print(termina_con) #Devuelve True porque la cadena termina con "do"


#METODOS QUE MODIFICAN EL CONTENIDO DE LA CADENA

#Metodo replace()
'''
El metodo replace() remplaza una subcadena por otra. Si la subcadena no esta dentro de la cadena
no la modifica
'''
#ejemplo:
cadena = "Hola Mundo"
reemplazar = cadena.replace("Mundo", "Luis")
print(reemplazar) 

#ejemplo 2:
cadena = "1,2,3,4,5,6"
print (cadena)
reemplazar = cadena.replace(",", " ")
print(reemplazar)

#Metodo split()
'''
El metodo split() divide la cadena y crea una lista, utilizando como separador la subcadena que le indiquemos
'''
#ejemplo:
cadena = "a-b-c-d-e-f"
cadena_separada = cadena.split("-")
print(cadena_separada)

