#area de un circulo

import math

radio = float(input("Ingrese el radio del circulo: "))

area = math.pi * radio**2
area = round(area, 2)
print(f"El area del circulo es: {area}")

longitud = 2 * math.pi * radio
longitud = round(longitud, 2)
print(f"La longitud del circulo es: {longitud}")

#otra manera de redondear es usando :.(numeros de decimales)f
#ejemplo: print(f"El area del circulo es: {area:.2f}")