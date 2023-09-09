# Conjuntos
# Un conjunto es una colección DESORDENADA de elementos únicos.
# A diferencia de las demas colecciones, los conjuntos no permiten elementos duplicados.

#creación de un conjunto

conjunto_1 = set() #crea un conjunto vacio

conjunto_1 = {15, "hola mundo", 41.1, True} #no se puede agregar una lista dentro de un conjunto 

#se deben crear esas 2 lineas necesariamente para crear un conjunto

print(conjunto_1) #imprime el tipo de dato

#nota: si colocas valores y se repiten solo imprime una vez ese valor
#ejemplo

conjunto_2 = set ()
conjunto_2 = {15,15,15,15,15,15,"luis", "luis", "luis"}

print(conjunto_2) #imprime solo una vez el valor


#AGREGAR ELEMENTOS A UN CONJUNTO

conjunto_3 = set()
conjunto_3 = {1,2,3,4,5,"a"}

# nombredelconjunto.add()
#ejemplo

conjunto_3.add(6) #agrega el valor 6 al conjunto
conjunto_3.add("hola")
conjunto_3.add("LUIS")
conjunto_3.add(3.1416)
print(conjunto_3)
#debes tener en cuenta que los conjuntos no se pueden ordenar
#por eso es que al añadir un elemento al conjunto no se sabe en que posicion se va a colocar


#ELIMINAR ELEMENTOS DE UN CONJUNTO

# nombredelconjunto.discard((elemento a eliminar))
#ejemplo

conjunto_4 = set()
conjunto_4 = {1,2,3,4,5,"a"}
conjunto_4.discard("a")
print(conjunto_4)

#ELIMINAR TODOS LOS ELEMENTOS DE UN CONJUNTO
# nombredelconjunto.clear()
#ejemplo

conjunto_5 = set()
conjunto_5 = {1,2,3,4,5,"a"}
conjunto_5.clear()
print(conjunto_5)


#DETERMINAR SI UN ELEMENTO ESTA EN UN CONJUNTO
#Ejemplo

conjunto_6 = set()
conjunto_6 = {1,2,3,4,5,"a"}
print("a" in conjunto_6)   #imprime true si el elemento esta en el conjunto y false si no esta
print("a" not in conjunto_6)    #imprime false si el elemento esta en el conjunto y true si no esta
