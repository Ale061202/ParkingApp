from Parking.entidades.cliente import Cliente
class Abonado(Cliente):

    def __init__(self,matricula,tipoV,activo,dni,nombre,apellidos,tarjetaCredito,abono,email,pin,plaza,fechaSuscripcion,fechaCancelacion):
        super().__init__(matricula,tipoV)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__tarjetaCredito = tarjetaCredito
        self.__abono = abono
        self.__email = email
        self.__pin = pin
        self.__plaza = plaza
        self.__fechaSuscripcion = fechaSuscripcion
        self.__fechaCancelacion = fechaCancelacion
        self.__activo = activo

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def tarjetaCredito(self):
        return self.__tarjetaCredito

    @tarjetaCredito.setter
    def tarjetaCredito(self, tarjetaCredito):
        self.__tarjetaCredito = tarjetaCredito

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, abono):
        self.__abono = abono

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def fechaSuscripcion(self):
        return self.__fechaSuscripcion

    @fechaSuscripcion.setter
    def fechaSuscripcion(self, fechaSuscripcion):
        self.__fechaSuscripcion = fechaSuscripcion

    @property
    def fechaCancelacion(self):
        return self.__fechaCancelacion

    @fechaCancelacion.setter
    def fechaCancelacion(self, fechaCancelacion):
        self.__fechaCancelacion = fechaCancelacion

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self,activo):
        self.__activo = activo