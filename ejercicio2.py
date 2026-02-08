asistencias = [
    ("Matemáticas", "Juan", "2024-09-01"),
    ("Matemáticas", "Ana", "2024-09-01"),
    ("Física", "Juan", "2024-09-01"),
    ("Matemáticas", "Juan", "2024-09-02"),
    ("Física", "Ana", "2024-09-02")
]
alumnos_asignatura = {}
for registro in asistencias:
    asignatura = registro[0]
    alumno = registro[1]
    
    if asignatura in alumnos_asignatura:
        alumnos_asignatura[asignatura].add(alumno)
    else:
        alumnos_asignatura[asignatura] = {alumno}
print(alumnos_asignatura)

dias_por_alumnos = {}

for registro in asistencias:
    alumno = registro[1]
    fecha = registro[2]
    
    if alumno in dias_por_alumnos:
        dias_por_alumnos[alumno].add(fecha)
    else:
        dias_por_alumnos[alumno] = {fecha}
        
print(dias_por_alumnos)

max_asistencias = 0
mejor_alumno = ""
for alumno in dias_por_alumnos:
    canridad = len(dias_por_alumnos[alumno])
    if canridad > max_asistencias:
        max_asistencias = canridad
        mejor_alumno = alumno
print(f"El alumno con mas asistencias es {mejor_alumno} con {max_asistencias} dias de asistencia")