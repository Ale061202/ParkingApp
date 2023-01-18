class Plaza:

    def __init__(self,id,reservado,ocupado,tipo):
        self.__id = id
        self.__reservado = reservado
        self.__ocupado = ocupado
        self.__tipo = tipo

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
    def ocupado(self):
        return self.ocupado

    @ocupado.setter
    def ocupado(self,ocupado):
        self.__ocupado = ocupado

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo