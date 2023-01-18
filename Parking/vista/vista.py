def menuPrincipal():
    print("Bienvenido, indique como va a acceder al aparcamiento:")
    print("1. Administrador")
    print("2. Cliente")
    print("0. Salir")

def menuCliente():
    print("Indique lo que quiere hacer:")
    print("1. Depositar un vehiculo")
    print("2. Retirar un vehiculo")
    print("3. Depositar un vehiculo abonado")
    print("4. Retirar un vehiculo abonado")
    print("0. Salir")

def menuAdmin():
    print("Indique lo que quiere hacer:")
    print("1. Consultar la situacion del parking")
    print("2. Consultar facturacion")
    print("3. Consultar abonados")
    print("4. Gestion abonos")
    print("5. Caducidad de los abonos")
    print("0. Salir")

def tiposVehiculos():
    print("Indique que vehiculo conduce:")
    print("1. Turismo")
    print("2. Motocicleta")
    print("3. Vehiculo para personas con movilidad reducida")

def menuAbonados():
    print("1. Dar de alta un abonado")
    print("2. Modificar los datos de un abonado")
    print("3. Dar de baja a un abonado")

def confirmacionBajaAbonado(fechaBajaAbonado):
    print(f"El cliente todavia tiene una suscripcion hasta el {fechaBajaAbonado.strftime('%d de %B del %Y')}.")
    print("Este cliente perdera su abono inmediatamente a pesar de que todavia tiene tiempo.")
    print("¿Estas seguro que quieres dar de baja a este cliente?")
    print("1. Si")
    print("2. No")

def abonadoQueCaduca(caducacion):
    for c in caducacion:
        print(f"{c.nombre} {c.apellidos} . Tipo de Abono : {c.abono.nombre} . Fecha de caducidad : {c.fechaCancelacion.strftime('%d de %B del %Y')}")

def plazasDeParking(plaza):
    plazaPos = 1
    for p in plaza:
        if plazaPos < 5:
            print(f" {p.id} - {p.estado.value} ", end=" ")
            plazaPos += 1
        else:
            print(f" {p.id} - {p.estado.value} ")
            plazaPos = 1

def CobrarPlazas(cobrar):
    for c in cobrar:
        print(
            f"Plaza {c.idPlaza.id}({c.plaza.plazaTipo.tipoV.value}) - {c.entrada.strftime('%d/%m/%Y, %H:%M:%S')} hasta {c.salida.strftime('%d/%m/%Y, %H:%M:%S')} - Total = {c.costeTicket} €")

def ListaDeAbonados(abonados):
    if len(abonados) == 0:
        print("No hay ningun abonado actualmente.")
    for a in abonados:
        print(
            f"{a.nombre} {a.apellidos}: Suscripcion {a.tipoAbono.nombre}, caduca el {a.fechaCancelacion.strftime('%d de %B del %Y')}")

def printPlazasDisponibles(plazasDisponibles, plazasTurismo, plazasMotos, plazasMovilidadReducida):
    print(f"Hay un total de {len(plazasDisponibles)} plazas disponibles")
    print(
        f"Estas son las plazas disponibles para los turismos: {plazasTurismo}." if plazasTurismo > 0 else "NO hay ninguna plaza disponible para los turismos")
    print(
        f"Estas son las plazas disponibles para motos: {plazasMotos}." if plazasMotos > 0 else "No hay ninguna plaza disponible para las motos")
    print(
        f"Estas son las plazas disponibles para vehículos para personas con movilidad reducidad: {plazasMovilidadReducida}." if plazasMovilidadReducida > 0 else "No hay ninguna plaza disponible para los vehiculos para personas con movilidad reducidad")


