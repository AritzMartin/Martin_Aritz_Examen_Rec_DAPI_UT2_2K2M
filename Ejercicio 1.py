import csv

countries_dict = {'30': 'Grecia', '33': 'Francia', '34': 'España', '351': 'Portugal', '380': 'Ucrania',
                  '39': 'Italia', '41': 'Suiza', '44': 'Reino Unido', '49': 'Alemania', '7': 'Rusia'}

nif_dict = {"0": "T", "1": 'R', "2": 'W', "3": 'A', "4": 'G', "5": 'M', "6": 'Y',
            "7": 'F', "8": 'P', "9": 'D', "10": 'X', "11": 'B', "12": 'N', "13": 'J',
            "14": 'Z', "15": 'S', "16": 'Q', "17": 'V', "18": 'H', "19": 'L', "20": 'C', "21": 'K', "22": 'E'}

def check_DGT(direccion):
    """"Esta función se dedica a abrir el documento, a leerlo y partir los datos; y finalmente cerrar el archivo.
    :param direccion: Es la dirección que tiene el archivo dentro de la carpeta donde esta guardada.
    :return Te devuelve los datos que ha corregido y los sobreescribe en el archivo original.
    """
    with open(direccion, 'r', encoding='utf-8') as file:
        fichero = file.readlines()
        fichero_partido = []
    with open(direccion, 'w', encoding='utf-8', newline='') as documento:
        titulos = ['Nombre', 'Apellidos', 'DNI', 'Teléfono', 'País', 'Vehículo', 'Multas Radar',
                   'Multas ITV', 'Multas Estupefacientes', 'Total Multas']
        escribir = csv.DictWriter(documento, fieldnames=titulos)
        escribir.writeheader()
        for datos in fichero:
            fichero_partido.append(datos.split(','))
        lista_final = []
        for lista in fichero_partido:
            dict_lista = {}
            dict_lista['Nombre'] = lista[0]
            dict_lista['Apellidos'] = lista[1]
            dict_lista['DNI'] = lista[2]
            dict_lista['Teléfono'] = lista[3]
            dict_lista['Vehículo'] = lista[4]
            dict_lista['Multas Radar'] = lista[5]
            dict_lista['Multas ITV'] = lista[6]
            dict_lista['Multas Estupefacientes'] = lista[7]
            lista_final.append(dict_lista)

        lista_final.pop(0)

        for datos_dgt in lista_final:
            datos_dgt['Nombre'] = check_username(datos_dgt['Nombre'])
            datos_dgt['Apellidos'] = check_username(datos_dgt['Apellidos'])
            datos_dgt['Teléfono'] = check_phone(datos_dgt['Teléfono'])
            datos_dgt['DNI'] = check_nif(datos_dgt['DNI'])
            datos_dgt['Total Multas'] = calculate_bill(datos_dgt['Multas Radar'], datos_dgt['Multas ITV'],
                                                       datos_dgt['Multas Estupefacientes'])

            escribir.writerow(datos_dgt)
    return

def check_username(nombre):
    """""
    Esta función tiene el objetivo de Capitalizar los nombres y apellidos que metamos.
    :param nombre: Nombre introducido.
    :return Nombre y apellidos capitalizados.
    """
    return nombre.title()

def check_nif(usuario_nif):
    """"Esta determina si la letra asociada al número del DNI es correcta; si no lo es lo corrige.
    :param usuario_nif: Los datos del DNI introducido.
    :return El DNI corregido.
    """
    return str(usuario_nif[0:8] + nif_dict[str(int(usuario_nif[0:8]) % 23)])

def check_phone(nun_completo):
    """"Esta función determina el país del prefijo y cambia el formato del teléfono introducido.
    :param nun_completo: Número de teléfono introducido.
    :return Nombre del país al que le pertenece el prefijo y el número de teléfono ordenado.
    """
    separacion1 = nun_completo.split('(')
    separacion2 = separacion1[1].split(')')
    separacion3 = separacion2[1].split('-')
    prefijo = separacion2[0]
    numero = separacion3[0] + separacion3[1]
    nom_prefijo = countries_dict[prefijo]
    telefono = '+' + prefijo + '-' + numero
    return nom_prefijo + ' ' + telefono

def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """"Esta función determina la cantidad a pagar después de la suma de todas las multas.
    :param multas_radar: Un (int) del volor a pagar por la multa de radar.
    :param multas_ITV: Un (int) del volor a pagar por la multa de ITV.
    :param multas_estupefacientes: Un (int) del volor a pagar por la multa de estupefacientes.
    :return La suma de las multas (int).
    """
    bill = int(multas_radar) + int(multas_ITV) + int(multas_estupefacientes)
    return bill

check_DGT("C:\datos\Documents\Aritz Martin 2M\DAPI\Recuperacion_DAPI_AritzMartin\Aritz Martin Girona - DGT.csv")

help(check_DGT)
help(check_username)
help(check_nif)
help(check_phone)
help(calculate_bill)
