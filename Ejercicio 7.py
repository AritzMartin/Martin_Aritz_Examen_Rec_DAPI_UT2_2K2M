def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """"Esta función determina la cantidad a pagar después de la suma de todas las multas.
    """
    bill = int(multas_radar + multas_ITV + multas_estupefacientes)
    return print(bill)
#quitar el print

multas_radar = int(input('Multa Radar: '))
multas_ITV = int(input('Multa ITV: '))
multas_estupefacientes = int(input('Multa Estupefacientes: '))

calculate_bill(multas_radar, multas_ITV, multas_estupefacientes)