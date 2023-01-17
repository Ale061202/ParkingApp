class Abonado:

    def __init__(self,matricula,tipo,dni,nombre,apellidos,tarjetaCredito,tipoAbono,email):
        self.matricula = matricula
        self.tipo = tipo
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.tarjetaCredito = tarjetaCredito
        self.tipoAbono = tipoAbono
        self.email = email

    def __str__(self):
        return '{}{}{}{}{}{}{}{}'.format(self.matricula,self.tipo,self.dni,self.nombre,self.apellidos,self.tarjetaCredito,self.tipoAbono,self.email)