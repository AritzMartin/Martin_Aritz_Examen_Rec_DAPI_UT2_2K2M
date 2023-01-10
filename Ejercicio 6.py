countries_dict = {'30': 'Grecia', '33': 'Francia', '34': 'España', '351': 'Portugal', '380': 'Ucrania',
                  '39': 'Italia', '41': 'Suiza', '44': 'Reino Unido', '49': 'Alemania', '7': 'Rusia'}

def check_phone(nun_completo):
    separacion1 = nun_completo.split('(')
    separacion2 = separacion1[1].split(')')
    separacion3 = separacion2[1].split('-')
    prefijo = separacion2[0]
    numero = separacion3[0] + separacion3[1]
    nom_prefijo = countries_dict[prefijo]
    telefono = '+' + prefijo + '-' + numero
    return print(nom_prefijo + ' ' + telefono)

num_completo = input('Introduce un número\n')
check_phone(num_completo)
#(33)3659-987