'''Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos
por ultimo mostrar la lista'''

lista = [1,2,3,3,3,3,3,3,3,2,1,4,5, "luis", "luis", 14.5,5.5,"maria", "maria"]

#transformar la lista en un conjunto
conjunto = set(lista)

#transformar el conjunto en una lista
lista = list(conjunto)

print(lista)

#OTRA FORMA
lista_1 = [1,2,3,3,3,3,3,3,3,2,1,4,5, "luis", "luis", 14.5,5.5,"maria", "maria"]
lista_1 = list(set(lista_1)) #transforma la lista en un conjunto y luego el conjunto en una lista
print(lista_1)
