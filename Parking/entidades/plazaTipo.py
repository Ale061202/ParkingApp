class plazaTipo:

    def __init__(self,numero,porcentaje,precioPlaza,tipoV):
        self.numero = numero
        self.porcentaje = porcentaje
        self.precioPlaza = precioPlaza
        self.tipoV = tipoV

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def porcentaje(self):
        return self.__porcentaje

    @porcentaje.setter
    def porcentaje(self,porcentaje):
        self.__porcentaje = porcentaje

    @property
    def precioPlaza(self):
        return self.__precioPlaza

    @precioPlaza.setter
    def precioPlaza(self,precioPlaza):
        self.__precioPlaza = precioPlaza

    @property
    def tipoV(self):
        return self.__tipoV

    @tipoV.setter
    def tipoV(self,tipoV):
        self.__tipoV = tipoV