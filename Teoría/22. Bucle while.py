# Bucle while (mientras)
# El bucle while se ejecuta mientras la condición sea verdadera
# Ejemplo


import math

r1 = int(input("Ingrese un numero: "))

while r1<0:
    print("Error")
    r1 = int(input("Ingrese un numero: "))
    
r2 = math.sqrt(r1)
round(r2,2)
print(r2)


#como iterador o repetidor
#se usa un iterador para repetir un proceso

i=0
while i<5:
    print(f"hola usuario n°{i}")
    i = i+1
    




