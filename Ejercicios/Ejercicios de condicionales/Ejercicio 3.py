letra = input("Ingrese una letra: ")

#pero con este metodo solo es valido para vocales en minuscula
#asi que usaremos el .lower para que la letra ingresada se convierta en minuscula

letra = letra.lower() #con esto convertimos la letra ingresada en minuscula

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("La letra ingresada es una vocal")
    
else:
    print("La letra ingresada es una consonante")
    
#pero tambien tenemos el .upper que convierte la letra ingresada en mayuscula