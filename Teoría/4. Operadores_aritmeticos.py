#operadores aritméticos

a = 5
b = 3

#suma
resultado = a + b
print(resultado)

#resta
resultado = a - b
print(resultado)

#multiplicación
resultado = a * b
print(resultado)

#división (con decimales)
resultado = a / b
print(resultado)

#división entera (me da el resultado de la división pero sin decimales, osea el cociente)
resultado = a // b
print(resultado)

#modulo (me da el residuo de la división)
resultado = a % b
print(resultado)

#exponente
resultado = a ** b
print(resultado)

'''
prioridad de los operadores aritméticos
1. ()
2. **
3. *, /, //, %
4. +, -
'''
#ejemplo
resultado = 3**3 * (13/5 - (2*4))
print(resultado)
