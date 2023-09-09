a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

r1 = a ** 3
r2 = (b ** 2) - 2 * a * c
r3 = 2 * b

resultado = (r1 * r2) / r3
print(f"El resultado es: {resultado}")
print("El resultado es: {}".format(resultado))