alumnos=[
    ("Juan", [7, 8, 9, 6], 90),
    ("Maria", [5, 6, 4, 7], 60),
    ("Pedro", [1, 9, 4, 7], 95),
    ("Ana", [6, 5, 7, 8], 85)
]
cantidad=4
cantNotas=4
def promedio(notas, cantNotas):
    suma=0
    i=0
    while i<cantNotas:
        suma=suma+notas[i]
        i=i+1
    return suma/cantNotas
def esRegular(alumno):
    nombre, notas, asistencia=alumno
    if promedio(notas, cantNotas)>=6 and asistencia>=75:
        return True
    else:
        return False
print("Alumnos:")
i=0
while i<cantidad:
    print(i+1, alumnos[i][0])
    i=i+1
numero=int(input("Numero del alumno a consultar: "))-1
if esRegular(alumnos[numero]):
    print(alumnos[numero][0], "esta regular")
else:
    print(alumnos[numero][0], "no esta regular")
