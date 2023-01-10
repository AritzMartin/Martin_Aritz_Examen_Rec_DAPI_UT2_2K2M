def check_username(nombre, apellidos):
    """""
    Esta función tiene el objetivo de Capitalizar los nombres y apellidos que metamos.
    :param nombre: Nombre introducido.
    :param apellidos: Apellidos introducidos.
    :return Nombre y apellidos capitalizados.
    """
    return nombre.title(), apellidos.title()
#quitar el print
#poner el help
nombre = input('Cual es tu nombre?\n')
apellidos = input('Cuales son tus apellidos?\n')
print(check_username(nombre, apellidos))