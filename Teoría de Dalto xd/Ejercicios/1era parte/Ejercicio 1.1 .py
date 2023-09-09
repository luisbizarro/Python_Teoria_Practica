#datos
horas_curso_actual = float(input("Ingrese las horas del curso actual:"))
horas_curso_minimo = 2.5
horas_curso_maximo = 7
horas_curso_promedio = 4

#diferencias de porcentaje

#a
dif_1 = (abs(horas_curso_actual-horas_curso_minimo))/horas_curso_minimo*100

print(f"La diferencia de horas del curso actual con el mínimo es de {dif_1}%")

dif_2 = (abs(horas_curso_actual-horas_curso_maximo))/horas_curso_maximo*100

print(f"La diferencia de horas del curso actual con el máximo es de {dif_2}%")

dif_3 = (abs(horas_curso_actual-horas_curso_promedio))/horas_curso_promedio*100

print(f"La diferencia de horas del curso actual con el promedio es de {dif_3}%")





