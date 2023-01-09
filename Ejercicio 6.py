def check_phone(nun_completo):
    separacion1 = nun_completo.split(sep=')')
    separacion2 = nun_completo.split(sep=')')
    prefijo = separacion1[0]
    numero = separacion2[1]
    return print(prefijo, numero)

num_completo = input('Introduce un número\n')
check_phone(num_completo)