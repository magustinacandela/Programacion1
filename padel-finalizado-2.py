import json

def leer_jugadores():
    arch = open("jugadores.json", "a+")
    arch.seek(0)
    texto = arch.read()
    arch.close()
    if texto == "":
        return []
    return json.loads(texto)

def escribir_jugadores(lista):
    arch = open("jugadores.json", "w")
    json.dump(lista, arch)
    arch.close()

def leer_parejas():
    arch = open("parejas.json", "a+")
    arch.seek(0)
    texto = arch.read()
    arch.close()
    if texto == "":
        return []
    return json.loads(texto)

def escribir_parejas(lista):
    arch = open("parejas.json", "w")
    json.dump(lista, arch)
    arch.close()

def registrar_participantes(lista):
    total = int(input("¿Cuántos jugadores van a participar en el torneo?: "))
    for i in range(total):
        print("Jugador", i + 1)
        nombre = input("Nombre: ")
        categoria = input("Categoría (4, 5, 6): ")
        participante = {"nombre": nombre, "categoria": categoria}
        lista.append(participante)
    escribir_jugadores(lista)
    print("Jugadores guardados con éxito.")

def ver_participantes(lista):
    if len(lista) == 0:
        print("No hay jugadores inscriptos.")
    else:
        print("LISTA DE INSCRIPTOS")
        for i in range(len(lista)):
            print(i + 1, ")", lista[i]["nombre"], "categoria:", lista[i]["categoria"])

def buscar_participante(lista):
    busqueda = input("Ingrese el nombre del jugador a buscar: ")
    encontrado = False
    for participante in lista:
        if participante["nombre"] == busqueda:
            print("El jugador", participante["nombre"], "está inscripto en la categoría", participante["categoria"])
            encontrado = True
            break
    if not encontrado:
        print("El jugador no está inscripto.")

def quitar_participante(lista):
    nombre = input("Ingrese el nombre del jugador lesionado a eliminar: ")
    encontrado = False
    for participante in lista:
        if participante["nombre"] == nombre:
            lista.remove(participante)
            escribir_jugadores(lista)
            print("Jugador eliminado correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró al jugador.")

def generar_parejas(jugadores, parejas):
    if len(jugadores) < 2:
        print("No hay suficientes jugadores para armar parejas.")
        return
    nombre_dupla = input("Ingrese el nombre de la pareja: ")
    ver_participantes(jugadores)
    p1 = int(input("Ingrese el número del primer jugador: ")) - 1
    p2 = int(input("Ingrese el número del segundo jugador: ")) - 1
    if p1 < 0 or p1 >= len(jugadores) or p2 < 0 or p2 >= len(jugadores):
        print("Número no válido.")
        return
    if p1 == p2:
        print("No puede elegir al mismo jugador dos veces.")
        return
    dupla = {
        "nombre": nombre_dupla,
        "jugadores": [jugadores[p1]["nombre"], jugadores[p2]["nombre"]]
    }
    parejas.append(dupla)
    escribir_parejas(parejas)
    print("Pareja armada y guardada con éxito.")

def ver_parejas(parejas):
    if len(parejas) == 0:
        print("No hay parejas armadas.")
    else:
        print("PAREJAS DEL TORNEO")
        for dupla in parejas:
            print("Pareja:", dupla["nombre"], "integrantes:", dupla["jugadores"][0], "y", dupla["jugadores"][1])

def main():
    jugadores = leer_jugadores()
    parejas = leer_parejas()
    opcion = ""
    while opcion != "7":
        print("MENU TORNEO DE PADEL")
        print("1. Registrar jugadores")
        print("2. Mostrar lista de inscriptos")
        print("3. Buscar jugador por nombre")
        print("4. Eliminar jugador (lesión)")
        print("5. Armar parejas")
        print("6. Mostrar parejas")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_participantes(jugadores)
        elif opcion == "2":
            ver_participantes(jugadores)
        elif opcion == "3":
            buscar_participante(jugadores)
        elif opcion == "4":
            quitar_participante(jugadores)
        elif opcion == "5":
            generar_parejas(jugadores, parejas)
        elif opcion == "6":
            ver_parejas(parejas)
        elif opcion == "7":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")

main()