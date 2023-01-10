def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """"Esta función determina la cantidad a pagar después de la suma de todas las multas.
    :param multas_radar: Un (int) del volor a pagar por la multa de radar.
    :param multas_ITV: Un (int) del volor a pagar por la multa de ITV.
    :param multas_estupefacientes: Un (int) del volor a pagar por la multa de estupefacientes.
    :return La suma de las multas (int).
    """
    bill = int(multas_radar + multas_ITV + multas_estupefacientes)
    return print(bill)
#quitar el print
#poner el help
multas_radar = int(input('Multa Radar: '))
multas_ITV = int(input('Multa ITV: '))
multas_estupefacientes = int(input('Multa Estupefacientes: '))

calculate_bill(multas_radar, multas_ITV, multas_estupefacientes)