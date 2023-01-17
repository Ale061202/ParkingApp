class Ticket:

    def __init__(self,matricula,tipo,fechaDeposito,idPlaza,pinDeSalida):
        self.matricula = matricula
        self.tipo = tipo
        self.fechaDeposito = fechaDeposito
        self.idPlaza = idPlaza
        self.pinDeSalida = pinDeSalida

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.tipo,self.matricula,self.fechaDeposito, self.idPlaza, self.pinDeSalida)