def check_username(nombre, apellidos):
    return nombre.title(), apellidos.title()
nombre = input('Cual es tu nombre?\n')
apellidos = input('Cuales son tus apellidos?\n')
print(check_username(nombre, apellidos))