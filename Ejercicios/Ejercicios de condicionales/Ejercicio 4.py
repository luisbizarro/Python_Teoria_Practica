n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))

operador = input("Ingrese el operador: (primera letra del operador) ")
operador = operador.lower()

if operador == "s":
    print("El resultado de la suma es: ", n1 + n2) 
    
elif operador == "r":
    print("El resultado de la resta es: ", n1 - n2)

elif operador == "p" or operador == "m":
    print("El resultado de la multiplicacion es: ", n1 * n2)
    
elif operador == "d":
    print("El resultado de la division es: ", n1 / n2)
    
    