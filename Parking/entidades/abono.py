
class Abono:
    def __init__(self,nombre,caducidad,precio):
        self.__nombre = nombre
        self.__caducidad = caducidad
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def caducidad(self):
        return self.__caducidad

    @caducidad.setter
    def caducidad(self,caducidad):
        self.__caducidad = caducidad

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,precio):
        self.__precio = precio