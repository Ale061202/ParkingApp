from datetime import datetime, timedelta

from Parking.entidades import abono, cliente, abonado, ticket, plaza
from Parking.entidades.enum import tipoV, estadoPlaza
from Parking.entidades.plazaTipo import plazaTipo


def config():

    numPlazas = 100
    plazasTurismos = plazaTipo(tipoV.TURISMO, 0.12, 70)
    plazasMotos = plazaTipo(tipoV.MOTOCICLETA, 0.08, 15)
    plazasMovilidad = plazaTipo(tipoV.MOVILIDADREDUCIDA, 0.10, 15)
    tiposPlazas = [plazasTurismos, plazasMotos, plazasMovilidad]
    plazas = []
    tickets = []
    clientes = []
    precio = 0

    abonos = []
    mensual = abono("Mensual", 1, 25.0)
    trimestral = abono("Trimestral", 3, 70.0)
    semestral = abono("Semestral", 6, 130.0)
    anual = abono("Anual", 12, 200.0)
    abonos.append(mensual)
    abonos.append(trimestral)
    abonos.append(semestral)
    abonos.append(anual)


    for tipo in tiposPlazas:
        precio += 1000
        tipo.numPlazas = int(numPlazas * (tipo.porcentajePlazas / 100))
        for i in range(tipo.numPlazas):
            plazas.append(plaza(precio + i, tipo))

    clienteNormal = cliente("618A", tipoV.TURISMO)
    clienteAbonado = abonado("123A", tipoV.TURISMO, "77941903D", "Alejandro", "Fernandez", "alejandro@gmail.com", "789123456789", semestral, datetime.now() - timedelta(days = 30), datetime.now() + timedelta(days = 180), True, plazas[2], 123456)
    clientes.append(clienteNormal)
    clientes.append(clienteAbonado)
    plazas[3].estado = estadoPlaza.ABONOLIBRE

    entrada = datetime.now() - timedelta(days=1, hours=3, minutes=45)
    salida = datetime.now() - timedelta(days=1, hours= 2, minutes=24)
    tiempoEstacionado = divmod((salida - entrada).total_seconds(), 60)[0]
    ocupacion1 = ticket(plazas[2], clienteAbonado, clienteAbonado.pin, datetime.now() - timedelta(days = 12), timedelta(days = 9), 0, False)
    ocupacion2 = ticket(plazas[0], clienteNormal, 763248, entrada, salida, tiempoEstacionado * plazas[0].plazaTipo.precioPlaza, False)
    ocupas.append(ocupacion1)
    ocupas.append(ocupacion2)