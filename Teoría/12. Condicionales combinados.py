#Condicionales combinados

#veamos un ejemplo para comprender

edad = int(input("Ingrese su edad: "))

if edad>0 and edad<=120: #edad entre 0 y 120 años
    print("Edad correcta")
    if edad >=18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Edad incorrecta")