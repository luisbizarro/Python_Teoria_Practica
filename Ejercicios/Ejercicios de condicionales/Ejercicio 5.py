sld_inicial = 1000

print("Bienvenido al cajero automatico")
print("¿Que desea hacer?")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

respuesta = int(input("Ingrese el numero de la opcion:"))

if respuesta == 1:
    print("¿Cuanto dinero desea ingresar?")
    
    dinero = int(input("Ingrese la cantidad: "))
    if dinero >= 0:
        sld_inicial = sld_inicial + dinero
        print("Su saldo actual es: ", sld_inicial)
    else:
        print("No se puede ingresar una cantidad negativa")
        
elif respuesta == 2:
    print("¿Cuanto dinero desea retirar?")
    dinero = int(input("Ingrese la cantidad: "))
    if dinero > sld_inicial:
        print("Saldo insuficiente")
    else:
        sld_inicial = sld_inicial - dinero
        print("Su saldo actual es: ", sld_inicial)

elif respuesta == 3:
    print ("Su saldo actual es: ", sld_inicial)
    
elif respuesta == 4:
    print("Gracias por usar el cajero automatico")

else:
    print("Opcion incorrecta")

