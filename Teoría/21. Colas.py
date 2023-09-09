# Colas (con listas)
# FIFO (First In First Out)
# El primero en entrar es el primero en salir
# ejemplo: una cola en el banco

#recordad el .pop() y el .append()
#.pop tiene la sintaxis .pop([i]) donde i es el indice del elemento a eliminar
#si no se especifica el indice, se elimina el ultimo elemento
#.append tiene la sintaxis .append(x) donde x es el elemento a agregar al final de la lista

#ejemplo

cola = ["Alejandro","Isabella", "Lucas", "Sofia", "Mateo"]
print(cola)

#agregando elementos a la cola
p1 = input("Introduzca un nombre: ")
p2 = input("Introduzca un nombre: ")

cola.append(p1)
cola.append(p2)
print(f"se agredo a {p1} y a {p2}")

print(cola)

#quitando elementos de la cola
e1 = cola.pop(0) #esto elimina el primer elemento de la cola
print(f"Estamos atendiendo a {e1}")
print(cola)
e2 = cola.pop(0)
print(f"Estamos atendiendo a {e2}")
print(cola)






