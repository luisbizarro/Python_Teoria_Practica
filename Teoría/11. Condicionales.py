# Condicionales
#Sirve para comparar valores

#if

'''
sintaxis

if condicion:       si se cumple la condicion entonces...
    codigo
elif condicion:     sino se cumple lo anterior entonces...
    codigo
else condicion:     sino se cumple TODOOOOO lo anterior entonces...
    codigo
    
'''

numero = int(input("Ingrese un numero: "))

if numero>0:
    print("El numero es positivo")
    numero = numero + 1
    print(f"El numero nuevo es: {numero}")
elif numero==0:
    print("El numero es cero")
else:
    print("El numero es negativo")
    
    