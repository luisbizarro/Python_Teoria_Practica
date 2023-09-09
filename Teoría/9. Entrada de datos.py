'''
1) creas la variable donde almacenar dicho valor
2) pides el valor al usuario
    con input("texto a mostrar")
3) lo almacenas en la variable
'''
#ejemplo

print("Hola ¿Cómo te llamas?")
nombre = input("coloca tu nombre: ") #tambien puedes guardar datos con espacios
print(f"Hola {nombre} mucho gusto")

#ojo este ejemplo solo funciona para guardar datos de tipo cadena, 
#en otras palabras no se puede modificar el tipo de dato
numero = input("coloca un numero: ")
print(f"el numero es {numero}")

#hasta ahí va bien, pero si quieres hacer una operacion con ese numero
#te dará un error, ya que el tipo de dato es cadena
#ejemplo
'''
numero = input("coloca un numero: ")
print(f"el numero es {numero}")
print(f"el numero + 5 es {numero + 5}")     {numero + 5} es un error

'''
#para solucionar esto, debes convertir el tipo de dato
#ejemplo
numero = int(input("coloca un numero: "))
print(f"el numero es {numero+10}")

#ojo, si colocas un numero con decimales, te dará un error
#para solucionar esto, debes convertir el tipo de dato
#ejemplo
numero = float(input("coloca un numero: "))
print(f"el numero es {numero+10.5}")    
