class Cliente:

    def __init__(self,matricula, tipoV):
        self.__matricula = matricula
        self.__tipoV = tipoV

    def __str__(self):
        return '{} con matricula {}'.format(self.tipoV,self.matricula)


    @property
    def tipoV(self):
        return self.__tipoV

    @tipoV.setter
    def tipoV(self,tipoV):
        self.__tipo = tipoV

    @property
    def matrciula(self):
        return self.__matrciula

    @matrciula.setter
    def matricula(self, matrciula):
        self.__matrciula = matrciula



