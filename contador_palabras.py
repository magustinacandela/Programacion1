parrafo=input('Ingrese el párrafo: ')
palabras=parrafo.split()
cantidad=0
for palabra in palabras:
    tiene_letra=False
    for letra in palabra:
        if letra>='a' and letra<='z' or letra>='A' and letra<='Z':
            tiene_letra=True
    if tiene_letra:
        cantidad=cantidad+1
print('Cantidad de palabras:', cantidad)