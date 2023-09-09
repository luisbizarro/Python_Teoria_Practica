#intercambiar el valor de 2 variables
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")

c = a
a = b
b = c


print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}") 