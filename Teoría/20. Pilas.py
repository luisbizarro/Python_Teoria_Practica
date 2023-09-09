#PILAS(CON LISTAS)
#para que tengas la idea de una pila, imagina una pila de platos, el ultimo plato que se pone es el primero que se saca
#esto es una pila, el ultimo elemento que se agrega es el primero que se saca
#para esto usaremos listas
#ejemplo

pila = [1,2]

#agregando elementos a la pila (los elementos se agregan al final de la lista)  
#se usa el metodo .append()

n1 = int(input("Introduzca un numero: "))
n2 = int(input("Introduzca un numero: "))
pila.append(n1)
pila.append(n2)
print("Se agrego el elemento {} y {} a la pila".format(n1,n2))
print(pila)

#sacando elementos de la pila (los elementos se sacan del final de la lista)
#se usa el metodo .pop()

b1 = pila.pop()
print("Se saco el ultimo elemento de la pila que es {}".format(b1))
print(pila)



