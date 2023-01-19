import random
import time
from datetime import datetime, timedelta
from threading import Thread

from Parking.entidades.abonado import Abonado
from Parking.entidades.cliente import Cliente
from Parking.entidades.enum.estadoPlaza import EstadoPlaza
from Parking.entidades.enum.tipoV import TipoV
from Parking.entidades.ticket import Ticket
from Parking.vista.vista import *
def principal():
    menuSelect = -1;

    clientes = []
    plaza = []
    ticket = []
    abonos = []

    while menuSelect != 0:

        submenu = -1;
        submenu2 = -1;
        submenu3 = 1;
        confirmacion = 1;
        menuPrincipal()
        try:
            menuSelect = int(input())
        except:
            print("Por favor introduzca un número.")

        if menuSelect == 1:

            while submenu != 0:

                menuCliente()
                try:
                    submenu = int(input())
                except:
                    print("Introduzca otro numero, por favor.")

                if submenu == 1:
                    plazaDisponibles = [plaza for plaza in plaza if plaza.estadoPlaza == EstadoPlaza.LIBRE]
                    turismosDisponibles = len([plaza for plaza in plazaDisponibles if plaza.plazaTipo.tipoV == TipoV.TURISMO])
                    motosDisponibles = len([plaza for plaza in plazaDisponibles if plaza.plazaTipo.tipoV == TipoV.MOTOCICLETA])
                    movilidadReducidaDisponibles = len([plaza for plaza in plazaDisponibles if plaza.plazaTipo.tipoV == TipoV.MOVILIDAD])
                    if len(plazaDisponibles) > 0:
                        plazasDisponibles(plazaDisponibles, turismosDisponibles, motosDisponibles, movilidadReducidaDisponibles)
                        tiposVehiculos()
                        try:
                            tipoVehiculo = list(TipoV)[int(input()) - 1]
                            if (tipoVehiculo == TipoV.TURISMO and turismosDisponibles > 0) or (tipoVehiculo == TipoV.MOTOCICLETA and motosDisponibles > 0) or (tipoVehiculo == TipoV.MOVILIDAD and movilidadReducidaDisponibles > 0) :
                                matricula = input("Introduzca su matrícula: ")
                                plaza = [plaza for plaza in plazaDisponibles if plaza.plazaTipo.tipoV == tipoVehiculo][0]
                                plaza.estadoPlaza = EstadoPlaza.OCUPADO
                                plazaOcupada = Ticket(plaza, Cliente(matricula, tipoVehiculo), random.randint(100000, 999999))
                                ticket.append(plazaOcupada)
                                print(f"Matricula: {plazaOcupada.cliente.matricula}, Vehículo: {plazaOcupada.cliente.tipoV} ,  Id: {plazaOcupada.plaza.id}, Pin: {plazaOcupada.pinSalida}")
                            else:
                                print("No hay plazas disponibles para ese vehículo")
                        except:
                            print("Por favor, introduzca un valor correcto de la lista de vehículos")
                    else:
                        print("No hay plazas disponibles para depositar el vehículo")

                elif submenu == 2:
                    try:
                        matricula = input("Por favor introduzca su matrícula: ")
                        numeroPlaza = int(input("Introduzca el número de la plaza de aparcamiento: "))
                        pin = int(input("Por último, introduzca el pin que se le proporcionó al estacionar: "))
                        ticketsEncontrados = [ticket for ticket in ticket if ticket.plaza.id == numeroPlaza and ticket.cliente.matricula == matricula and ticket.pinSalida == pin]
                        if(len(ticket) >= 1):
                            ticket = ticketsEncontrados[0]
                            ticket.ocupado = False
                            ticket.salida = datetime.now()
                            tiempoEstacionado = divmod((ticket.fechaSalida - ticket.fechaEntrada).total_seconds(), 60)[0]
                            ticket.costeTotal = ticket.plaza.plazaTipo.precioPlaza * tiempoEstacionado
                            ticket.idPlaza.estado = EstadoPlaza.LIBRE
                            print(f"El coste total ha sido de {ticket.coste} €")
                        else:
                            print("No se ha encontrado el vehículo estacionado.")
                    except:
                        print("Por favor introduzca una plaza válida y un pin válido")

                elif submenu == 3:
                    dni = input("Hola de nuevo, por favor, introduzca su dni: ")
                    matricula = input("Introduzca su matrícula: ")
                    try:
                        cliente = next(cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo and cliente.matricula == matricula and cliente.dni == dni)
                        print(f"Puede proceder a estacionar su vehiculo, su plaza es la {cliente.plaza.id}")
                        cliente.plaza = [plaza for plaza in plaza if plaza.id == cliente.plaza.id][0]
                        cliente.plaza.estadoPlaza = EstadoPlaza.OCUPADOABONO
                        ticket.append(Ticket(cliente.plaza, cliente, cliente.pin, coste=0))
                    except:
                        print("No se encuentra el vehículo con los datos proporcionados.")

                elif submenu == 4:
                    dni = input("Bienvenido de nuevo, por favor, introduzca su dni: ")
                    matricula = input("Introduzca su matrícula: ")
                    pin = input("Introduzca su pin: ")
                    try:
                        ticket = next(ticket for ticket in ticket if ticket.activo and ticket.pin == int(pin) and ticket.cliente.matricula == matricula and ticket.cliente.dni == dni)
                        print("Puede proceder a sacar su vehiculo")
                        cliente.plaza.estadoPlaza = EstadoPlaza.LIBREABONO
                        ticket.activo = False
                    except:
                        print("No se encuentra el vehículo con los datos que ha proporcionado.")

        elif menuSelect == 2:
            while submenu != 0:
                menuAdmin()
                try:
                    submenu = int(input())
                except:
                    print("Por favor, introduzca un número que se encuentre en la lista.")

                if submenu == 1:
                    plazaDisponibles = len([plaza for plaza in plaza if plaza.estadoPlaza == EstadoPlaza.LIBRE])
                    porcentajeOcupacion = (100 - plazaDisponibles) / (100/100)
                    print(f"Actualmente hay {plazaDisponibles} plazas disponibles, el porcentaje de ocupación es del {porcentajeOcupacion}%")
                    plazasDeParking(plaza)

                elif submenu == 2:
                    try:
                        print("Introduzca la fecha a partir de la que consultar.")
                        anioInicio = input("Año: ")
                        mesInicio = input("Mes: ")
                        diaInicio = input("Día: ")
                        horaInicio = input("Hora: ")
                        minutosInicio = input("Minutos: ")
                        inicio = datetime(int(anioInicio), int(mesInicio), int(diaInicio), int(horaInicio), int(minutosInicio))
                        print("Introduzca la fecha hasta la que consultar.")
                        anioFin = input("Año: ")
                        mesFin = input("Mes: ")
                        diaFin = input("Día: ")
                        horaFin = input("Hora: ")
                        minutosFin = input("Minutos: ")
                        final = datetime(int(anioFin), int(mesFin), int(diaFin), int(horaFin), int(minutosFin))
                        cobros = [ticket for ticket in ticket if (not ticket.activo) and (ticket.costeTotal > 0 and ticket.salida < final and ticket.salida > inicio)]
                        cobrarPlazas(cobros)
                    except:
                        print("Ha habido un error al obtener las fechas. Por favor, indique el año, mes, dia, hora y minuto con un número.")

                elif submenu == 3:
                    clientesAbonados = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo]
                    listaDeAbonados(clientesAbonados)

                elif submenu == 4:
                    menuAbonados()
                    try:
                        submenu2 = int(input())
                    except:
                        print("Por favor introduzca un número.")

                    if submenu2 == 1:
                        dni = input("Dni del abonado: ")
                        nombre = input("Nombre del abonado: ")
                        apellidos = input("Apellidos del abonado: ")
                        email = input("Email del abonado: ")

                        try:
                            print("Seleccione el tipo de abono:")
                            for i, abono in enumerate(abonos):
                                print(f"{i+1}. {abono.nombre} - {abono.precio}€")
                            tipoAbono = abonos[int(input()) - 1]
                            tarjeta = input("Tarjeta del abonado: ")

                            tiposVehiculos()
                            tipoVehiculo = list(TipoV)[int(input()) - 1]
                            matricula = input("Matricula del vehículo: ")
                            plaza = next(plaza for plaza in plaza if plaza.estado == EstadoPlaza.LIBRE and plaza.plazaTipo.tipoV == tipoVehiculo)
                            pin = random.randint(100000, 999999)

                            nuevoCliente = Abonado(matricula, tipoVehiculo, dni, nombre, apellidos, email, tarjeta, tipoAbono, datetime.now(), datetime.now() + timedelta(days = 30 * tipoAbono.caducidad), True, plaza, pin)
                            clientes.append(nuevoCliente)
                            plaza.estado = EstadoPlaza.ABONOLIBRE
                            print("El cliente se ha suscrito con éxito.")
                        except:
                            print("Por favor, seleccione una opción que se encuentre en la lista.")

                    elif submenu2 == 2:
                        dni = input("Introduzca el DNI del abonado que vaya a modificar: ")
                        try:
                            abonado = next(cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo and cliente.dni == dni)
                            print("1. Modificar datos del cliente")
                            print("2. Renovar abono")
                            submenu3 = int(input())

                            if submenu3 == 1:
                                print("Introduzca los siguientes datos a continuación, para poder mantener su abono actual.")
                                abonado.dni = input(f"Dni del abonado (actual: {abonado.dni}): ") or abonado.dni
                                abonado.nombre = input(f"Nombre del abonado (actual: {abonado.nombre}): ") or abonado.nombre
                                abonado.apellidos = input(f"Apellidos del abonado (actual: {abonado.apellidos}): ") or abonado.apellidos
                                abonado.email = input(f"Email del abonado (actual: {abonado.email}): ") or abonado.email
                                abonado.matricula = input(f"Matricula del vehículo (actual: {abonado.matricula}): ") or abonado.matricula
                                abonado.tarjeta = input(f"Tarjeta del abonado (actual: {abonado.tarjeta}): ") or abonado.tarjeta

                            elif submenu3 == 2:
                                caducidadAntigua = abonado.fechaCancelacion
                                abonado.fechaCancelacion = caducidadAntigua + timedelta(days=30 * abonado.tipoAbono.duracion)
                                print(f"El abono {abonado.tipoAbono.nombre} del cliente con DNI {abonado.dni} caducaba el {caducidadAntigua.strftime('%d de %B del %Y')}")
                                print(f"Se ha extendido su abono por {abonado.tipoAbono.duracion} meses, la nueva fecha para cancelar su abono es el {abonado.fechaCancelacion.strftime('%d de %B del %Y')}")
                        except:
                            print("No se ha podido encontrar al cliente, puede que su dni sea erróneo o no es usted actualmente un abonado")

                    elif submenu2 == 3:
                        dni = input("Introduzca el DNI del abonado a dar de baja: ")
                        try:
                            abonado = next(
                                cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.dni == dni)
                            if abonado.activo:
                                confirmacionBajaAbonado(abonado.fechaCancelacion)
                                confirmacion = int(input())
                                if confirmacion == 1:
                                    abonado.plaza = [plaza for plaza in plaza if plaza.id == abonado.plaza.id][0]
                                    abonado.activo = False
                                    abonado.plaza.estadoPlaza = EstadoPlaza.LIBRE
                                    print("El cliente se ha dado de baja.")
                            else:
                                print("El cliente no tiene ningún abono activo.")
                        except:
                            print("No se ha podido encontrar al cliente")

                elif submenu == 5:
                    print("1. Consultar los abonos que caducan en un mes")
                    print("2. Consultar los abonos que caducan en menos de 10 días")
                    try:
                        submenu2 = int(input())
                    except:
                        print("Por favor introduzca un número.")

                    if submenu2 == 1:
                        mes = int(input("Indique el nº del mes que quiere consultar: "))
                        anio = int(input("Indique el año que quiere consultar: "))
                        aCaducar = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.fechaCancelacion.month == mes and cliente.fechaCancelacion.year == anio]
                        abonadoQueCaduca(aCaducar)
                        if len(aCaducar) == 0: print("No hay ningún cliente que su abono vaya a caducar en ese mes.")

                    elif submenu2 == 2:
                        aCaducar = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.fechaCancelacion > datetime.now() and cliente.fechaCancelacion < datetime.now() + timedelta(days = 12)]
                        abonadoQueCaduca(aCaducar)
                        if len(aCaducar) == 0: print("No hay ningún cliente que su abono vaya a caducar en 12 días.")

mainThread = Thread(target=principal)

mainThread.start()