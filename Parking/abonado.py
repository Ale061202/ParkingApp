from Parking.cliente import Cliente
class Abonado(Cliente):

    def __init__(self,matricula,tipoV,dni,nombre,apellidos,tarjetaCredito,tipoAbono,email,pin,plaza,fechaSuscripcion,fechaCancelacion):
        super().__init__(matricula,tipoV)
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.tarjetaCredito = tarjetaCredito
        self.tipoAbono = tipoAbono
        self.email = email
        self.pin = pin
        self.plaza = plaza
        self.fechaSuscripcion = fechaSuscripcion
        self.fechaCancelacion = fechaCancelacion

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
    def tipoAbono(self):
        return self.__tipoAbono

    @tipoAbono.setter
    def tipoAbono(self, tipoAbono):
        self.__tipoAbono = tipoAbono

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