cantidad=int(input("Ingresar la cantidad de jugadores: "))
if cantidad%2==1:
    print("La cantidad debe ser par")
    exit()
nombres=[""]*cantidad
categorias=[""]*cantidad
i=0
while i<cantidad:
    print("Jugador", i+1)
    nombres[i]=input("Nombre: ")
    categorias[i]=input("Categoria: ")
    i=i+1
print("Lista de jugadores")
i=0
while i<cantidad:
    print(i+1, nombres[i], categorias[i])
    i=i+1
cantParejas=cantidad//2
nombresParejas=[""]*cantParejas 
integrantesParejas=[""]*cantParejas
i=0
while i<cantParejas:
    print("Pareja", i+1)
    nombresParejas[i]=input("Nombre de la pareja: ")
    jugador1=int(input("Numero del primer jugador: ")) -1
    jugador2=int(input("Numero del segundo jugador: ")) -1
    if jugador1==jugador2 or jugador1<0 or jugador1>=cantidad or jugador2<0 or jugador2>=cantidad:
        print("Pareja invalida")
    else:
        integrantesParejas[i]=nombres[jugador1]+" y "+nombres[jugador2]
        i=i+1
print("Parejas formadas")
i=0
while i<cantParejas:
    print(nombresParejas[i], "-", integrantesParejas[i])
    i=i+1