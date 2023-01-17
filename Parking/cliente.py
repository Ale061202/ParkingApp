class SinAbono:

    def __init__(self,matricula, tipo):
        self.matricula = matricula
        self.tipo = tipo

    def __str__(self):
        return '{} con matricula {}'.format(self.tipo,self.matricula)



