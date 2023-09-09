a = float(input("a:"))
b = float(input("b:"))

r1 = (3+5*8)<3
r2 = (-6/3*4)+2<2
r3 = a > b

resultado = (r1 and r2) or r3

print(f"el resultado es: {resultado}")