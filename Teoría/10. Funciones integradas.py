#funciones integradas

#int (lo que ingresa el usuario se convierte en un numero entero)
numero = int(input("coloca un numero: "))
print(f"el numero es {numero+10}")

#float (lo que ingresa el usuario se convierte en un numero decimal)
numero = float(input("coloca un numero: "))
print(f"el numero es {numero+10.5}")

#str (lo que ingresa el usuario se convierte en una cadena)
#ojo no se puede realizar operaciones aritmética con este tipo de dato
numero = str(input("coloca un numero o texto: "))
print(f"el numero es {numero}")

#los ejemplos a continuación se pueden usar con input, solo que lo hago
#con variables para que se vea mas claro

#bin (transforma un numero a binario)
numero = bin(10)
print(numero)

#hex (transforma un numero a hexadecimal)
n = hex(10)
print(n)

#int (transforma un numero de otra base a base 10)
#sintaxis int(numero, base) base es opcional porque por defecto es 10
n = int("0b1010", 2)
print(n)

n = int("0xa", 16)
print(n)

n = int(5)
print(n)

#abs (devuelve el valor absoluto de un numero)
n = abs(-10)
print(n)

#round (redondea un numero decimal a entero)
    #sintaxis round(numero, numero de decimales)
n = round(5.67) #si colocas el numero lo redondea al entero mas cercano
print(n)

n = round(5.67, 1) #si colocas el numero lo redondea al entero mas cercano
print(n)

#len (devuelve la cantidad de caracteres de una cadena)
#posdata: los espacios cuentan como caracteres
n = len("hola mundo")
print(n)
