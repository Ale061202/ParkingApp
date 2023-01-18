from Parking.entidades.enum.estadoPlaza import EstadoPlaza
class Plaza:

    def __init__(self,id,reservado,estadoPlaza = EstadoPlaza.LIBRE):
        self.__id = id
        self.__reservado = reservado
        self.__estadoPlaza = estadoPlaza

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def reservado(self):
        return self.__reservado

    @reservado.setter
    def reservado(self,reservado):
        self.__reservado = reservado

    @property
    def estadoPlaza(self):
        return self.__estadoPlaza

    @estadoPlaza.setter
    def estadoPlaza(self,estadoPlaza):
        self.__estadoPlaza = estadoPlaza