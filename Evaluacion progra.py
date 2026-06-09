total_estudiantes = 0
aprobados = 0
rep_nota = 0
rep_asistencia = 0

continuar = "S"

while continuar.upper() == "S":

    print("\nREGISTRO DE ESTUDIANTE")

    nombre = input("Nombre completo: ")
    clases_programadas = int(input("Cantidad de clases programadas: "))
    clases_asistidas = int(input("Cantidad de clases asistidas: "))
    nota = float(input("Calificación final: "))

    asistencia = (clases_asistidas / clases_programadas) * 100

    if asistencia < 80:
        condicion = "Reprobado por asistencia"
        rep_asistencia += 1

    elif nota >= 51:
        condicion = "Aprobado"
        aprobados += 1

    else:
        condicion = "Reprobado por nota"
        rep_nota += 1

    print("\nRESULTADO")
    print("Nombre:", nombre)
    print("Asistencia:", round(asistencia, 2), "%")
    print("Condición:", condicion)

    total_estudiantes += 1

    continuar = input("\n¿Desea registrar otro estudiante? (S/N): ")

if total_estudiantes > 0:
    porcentaje_aprobados = (aprobados / total_estudiantes) * 100
else:
    porcentaje_aprobados = 0

print("\nRESUMEN FINAL")
print("Total de estudiantes:", total_estudiantes)
print("Aprobados:", aprobados)
print("Reprobados por nota:", rep_nota)
print("Reprobados por asistencia:", rep_asistencia)
print("Porcentaje de aprobados:", round(porcentaje_aprobados, 2), "%")