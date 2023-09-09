#Operadores de comparacion
#te devuelven un valor booleano (True o False)

# = asignacion
# == comparacion
# != diferente
# < menor que
# > mayor que
# <= menor o igual que
# >= mayor o igual que

diccionario = {
    "Persona 1": {
        "nombre": "Luis",
        "edad": 20,
        "estatura": 1.80,
        "peso": 80
    }
    ,
    "Persona 2": {
        "nombre": "Juan",
        "edad": 45,
        "estatura": 1.80,
        "peso": 80
    }
    ,
    "Persona 3": {
        "nombre": "Pedro",
        "edad": 20,
        "estatura": 1.80,
        "peso": 80
    }
    ,
    "Persona 4": {
        "nombre": "Maria",
        "edad": 21,
        "estatura": 1.80,
        "peso": 80
    }
    ,
    "Persona 5": {
        "nombre": "Luisa",
        "edad": 10,
        "estatura": 1.80,
        "peso": 80
    }
    
}

diccionario2 = {}
for i in range(2):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    estatura = float(input("Ingrese su estatura: "))
    peso = float(input("Ingrese su peso: "))
    diccionario2[nombre] = {edad, estatura, peso}
    
print(diccionario2)
