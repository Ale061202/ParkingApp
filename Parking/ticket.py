class Ticket:

    def __init__(self,cliente,pinSalida,fechaEntrada,fechaSalida,coste,idPlaza,pinSalida,ocupado):
        self.cliente = cliente
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida
        self.coste = coste
        self.idPlaza = idPlaza
        self.pinSalida = pinSalida
        self.ocupado = ocupado

    def __str__(self):
        return f"El vehiculo con matricula {self.cliente.matricula} entra a las {self.fechaEntrada}"

    @property
    def idPlaza(self):
        return self.__idPlaza

    @idPlaza.setter
    def idPlaza(self, idPlaza):
        self.__idPlaza = idPlaza

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def pinSalida(self):
        return self.__pinSalida

    @pinSalida.setter
    def pinSalida(self, pinSalida):
        self.__pinSalida = pinSalida

    @property
    def fechaEntrada(self):
        return self.__fechaEntrada

    @fechaEntrada.setter
    def fechaEntrada(self, fechaEntrada):
        self.__fechaEntrada = fechaEntrada

    @property
    def fechaSalida(self):
        return self.__fechaSalida

    @fechaSalida.setter
    def fechaSalida(self, fechaSalida):
        self.__fechaSalida = fechaSalida

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, ocupado):
        self.__ocupado = ocupado

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, coste):
        self.__coste = coste

