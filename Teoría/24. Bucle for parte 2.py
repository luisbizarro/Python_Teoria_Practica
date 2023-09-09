#Bucle for

#uso del range
#sintaxis 1: range(inicio, fin, salto)
#ejemplo:

for i in range(1, 10, 1):
    print(i, end=" ") #imprime del 1 al 9
    
#ejemplo 2:
print()
for i in range(10):
    print(i, end = " ") #imprime del 0 al 9
    
#ejemplo 3:
print()
for i in range(1, 10, 2):
    print(i, end = " ") #imprime del 1 al 9 de 2 en 2
    
#ejemplo 4:
print()
for i in range(10, 1, -1):
    print(i, end = " ") #imprime del 10 al 2 de 1 en 1
    
#ejemplo 5:
print()
for i in range(10, 1, -2):
    print(i, end = " ") #imprime del 10 al 2 de 2 en 2
    
#sintaixs 2: range(fin)

n=5 #numero de veces que se va a repetir el bucle = [0,5>

print()
for i in range(n):
    print(i, end = " ") #imprime del 0 al 4
    
#sintaxis 3: range(inicio, fin)
print()
for i in range(1, n):
    print(i, end = " ") #imprime del 1 al 4
    
#veamos un ejemplo con todo lo aprendido
#cree un programa que muestre la tabla de multiplicar con los datos del usuario
print()
multiplicando = int(input("Ingrese el multiplicando: "))
rango = int(input("Ingrese el rango: "))
for i in range(1, rango + 1):
    print(multiplicando, "x", i, "=", multiplicando * i)




