'''
Escriba un programa que tenga 2 listas y que a continuación, cree las siguientes listas (en las que no debe haber repeticiones):
- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas.
'''

notas_1 = [14,15,15,15,15,19,17,15]
notas_2 = [16,17,18,19,20,15,17,16,20]

notas_1 = set(notas_1)
notas_2 = set(notas_2)

#Lista de elementos que aparecen en las dos listas.
notas_de_las_secciones = list(notas_1 | notas_2)
notas_de_las_secciones.sort()
print("Las notas de las 2 secciones son: ", notas_de_las_secciones)

#Lista de elementos a-b
notas_de_la_seccion_1 = list(notas_1 - notas_2)
notas_de_la_seccion_1.sort()
print("Las notas de la sección 1 son: ", notas_de_la_seccion_1)

#Lista de elementos b-a
notas_de_la_seccion_2 = list(notas_2 - notas_1)  
notas_de_la_seccion_2.sort()
print("Las notas de la sección 2 son: ", notas_de_la_seccion_2)

#Lista de elementos que aparecen en ambas listas.
notas_de_ambas_secciones = list(notas_1 & notas_2)
notas_de_ambas_secciones.sort()
print("Las notas repetidas de las secciones son:", notas_de_ambas_secciones)