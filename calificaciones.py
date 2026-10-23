inscritos = int(input("Cantidad de alumnos en la clase: "))
casos_reprobados = 0
casos_regulares = 0
casos_buenos = 0
casos_excelentes = 0

for alumno in range(inscritos):
    suma_valoraciones = 0
    print(f"\nNotas del alumno {alumno + 1}:")
    
    for nota_individual in range(4):
        valoracion = float(input(f"Calificación {nota_individual + 1}: "))
        suma_valoraciones += valoracion
    
    media_estudiante = suma_valoraciones / 4.0
    print(f"Promedio obtenido: {media_estudiante:.2f}")

    if media_estudiante < 3.0:
        print("Desempeño: Reprobado.")
        casos_reprobados += 1
    elif 3.0 <= media_estudiante <= 4.0:
        print("Desempeño: Regular.")
        casos_regulares += 1
    elif 4.0 < media_estudiante <= 4.5:
        print("Desempeño: Bueno.")
        casos_buenos += 1
    else:
        print("Desempeño: Excelente.")
        casos_excelentes += 1

print("\nEstadísticas del grupo:")
print(f"Total reprobados: {casos_reprobados}")
print(f"Total regulares: {casos_regulares}")
print(f"Total buenos: {casos_buenos}")
print(f"Total excelentes: {casos_excelentes}")