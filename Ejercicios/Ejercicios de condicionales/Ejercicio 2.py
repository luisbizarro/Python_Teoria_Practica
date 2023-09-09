n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

if n1>n2 and n1>n3:
    print("El primer numero es el mayor")
elif n2>n1 and n2>n3:
    print("El segundo numero es el mayor")
elif n3>n1 and n3>n2:
    print("El tercer numero es el mayor")
else:
    print("Los numeros son iguales")


