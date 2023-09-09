
texto = input("Ingrese un texto: ")

#convertir string a lista
lista = texto.split(" ")
elementos = len(lista)
print(f"se ha encontrado {elementos} palabras y tardarías en decirlo {elementos/2} segundos")
#dato 1 segundo = 2 palabras
if elementos > 120:
    print("Mucho texto")
     