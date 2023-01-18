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

