compra = float(input("Ingrese el valor de la compra: "))
descuento = compra * 0.15
print(f"El valor del descuento es: {descuento:.2f}")
compra = compra - descuento
print(f"El valor de la compra con descuento es: {compra:.2f}")
