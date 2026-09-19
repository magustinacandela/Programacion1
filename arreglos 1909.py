estudiantes= [
    {"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90},
    {"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60},
    {"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95},
    {"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85},
]
for alumno in estudiantes: 
    nombre= alumno ["nombre"]
    notas= alumno ["notas"]
    asistencia= alumno ["asistencia"]
    promedio= suma= sum(notas) / len(notas)
    if notas[0] >= 6 and notas[1] >= 6 and notas[2] >= 6 and notas[3] >= 6 and promedio >= 6 and asistencia >= 75:
        print(nombre, "esta regular, su promedio es de", promedio, "y una asistencia de", asistencia)
    else:
        print(nombre, "no esta regular, su promedio es de", promedio, " y su asitencia es de", asistencia)