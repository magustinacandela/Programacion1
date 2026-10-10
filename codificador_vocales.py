texto=input('Ingrese el mensaje: ')
texto=texto.upper()
texto=texto.replace('Á', 'A')
texto=texto.replace('É', 'E')
texto=texto.replace('Í', 'I')
texto=texto.replace('Ó', 'O')
texto=texto.replace('Ú', 'U')
mensaje=''
for letra in texto:
    if letra=='A':
        mensaje=mensaje+'X'
    elif letra=='E':
        mensaje=mensaje+'W'
    elif letra=='I':
        mensaje=mensaje+'K'
    elif letra=='O':
        mensaje=mensaje+'&'
    elif letra=='U':
        mensaje=mensaje+'%'
    else:
        mensaje=mensaje+letra
print('Mensaje codificado:', mensaje)