Algoritmo registro_asistencia
	Definir saldo como real
    Definir opcion como entero
    Definir importe como real
	saldo<-50000
    Repetir
        Escribir ""
        Escribir "Cajero automatico"
        Escribir "1. Consultar saldo"
        Escribir "2. Depositar"
        Escribir "3. Extraer"
        Escribir "4. Salir"
        Escribir "Ingrese una opcion:"
        Leer opcion
        Segun opcion Hacer
            1:Escribir "Su saldo actual es: $", saldo
            2:Escribir "Ingrese el importe a depositar:"
			  Leer importe
			  Mientras importe <= 0 Hacer
                    Escribir "El importe tiene que ser mayor que cero"
                    Escribir "Ingrese el importe a depositar:"
                    Leer importe
			  Fin Mientras
                saldo<-saldo + importe
			  Escribir "El deposito se realizo correctamente y su saldo ahora es: $", saldo
            3:Escribir "Ingrese el importe a extraer:"
			  Leer importe
			  Mientras importe <= 0 Hacer
                    Escribir "El importe tiene que ser mayor que cero"
                    Escribir "Ingrese el importe a extraer:"
                    Leer importe
			  Fin Mientras
                Si importe <= saldo Entonces
					saldo<-saldo - importe
                    Escribir "La extraccion se realizo correctamente y su saldo ahora es: $", saldo
                SiNo
                    Escribir "Fondo insuficiente y su saldo actual es: $", saldo
                Fin Si
            4:Escribir "La opcion no es valida, ingrese un numero del 1 al 4"
        Fin Segun
    Hasta Que opcion=4
FinAlgoritmo