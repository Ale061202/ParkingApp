# ParkingApp

## ***Explicación***

Este es un ejercicio práctico para la gestión de un ***parking***. Para poder hacer la gestión del parking he creado las clases:

- Cliente: en cliente se guardan la matricula y el tipo de vehiculo que conduce el cliente
- Abonado: en abonado se guardan el dni, el nombre y apellidos del cliente abonado, el numero de su plaza, la matricula y el tipo de vehiculo...
- Abono: en el abono se guardan el precio del abono, el tiempo de caducidad y el tipo del abono (nombre)
- Ticket: en el ticket se guardan los datos del cliente que ocupa la plaza, la fecha y hora de entrada y de salida, el pin de salida, el coste total de la estancia del parking, los datos de la plaza.
- Plaza: en la plaza se guardan el identificador de la plaza, si esta reservado para un abonado, el tipo de la plaza y como se encuentra la plaza ej.(Libre,Ocupado...)
- PlazaTipo: en la plazaTipo se guardan el tipo de vehiculo, el porcentaje que se le aplica a la plaza, el precio de la plaza, el numero de la plaza.

Después de terminar la creación de las entidades, se hacen una serie de funciones como:

- Depositar un vehículo: para poder depositar un vehiculo de tipo cliente si es un cliente normal tendra que poner la matrícula y decir que tipo de vehiculo esta conduciendo.
- Retirar un vehículo: para poder retirar el vehiculo tienes que introducir la matricula, el identificador de la plaza y el pin que se muestra en el ticket
- Depositar un abonado: para poder depositar el vehiculo de un abonado se tiene que introducir la matricula y el dni del abonado.
- Retirar un abonado: para poder retirar el vehiculo de un abonado tiene que introducir la matricula, el identificador de la plaza y el pin de salida.
- Comprobar el estado del parking: en este método se muestra el número de plazas disponibles.
- Facturación: en el método se le pasan dos fechas que van a ser la fecha de entrada y salida y se realizara un cobro especial por cada tipo de plaza, a los abonados no se le contempla esta opción.
- Consultar los abonados: con este método vamos a ver los abonos que son temporales.
- Abonos: con este método damos de alta a un cliente pidiendole sus datos, y dependiendo de su abono se le cobrara un precio mayor o menor. También puedes modificar algún dato personal de abonado, y también si se puede dar de alta a un cliente se puede dar de baja a un abonado pero no se borraran sus datos.
- Caducidad de los abonos: introducimos un mes y el programa nos informará que abonos caducan este mes.

En un posible futuro se podrá añadir más funciones, espero que les sirva de ayuda.

## **Tecnología utilizada**

Para realizar este proyecto he utilizado:

1. [Python](https://python.org/)


