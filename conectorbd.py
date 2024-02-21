import mysql.connector
from mysql.connector import Error


class Conectar:
    def __init__(self) :
        try:
            self.conexion = mysql.connector. connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "Vicky@1996",
                database = "Reservaciones"
            )
        except Error as ex:
            print("No se puede concretar la conexion: {0}".format(ex))

    def listar(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select * from clientes")
                respuesta = cursor.fetchall()
                return respuesta
            except Error as ex:

                print("Error en el intento de conectar: {0}".format(ex))
    def registro (self, clientes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("insert into clientes ( id, dni, nombre, apellido, direccion ) values ({0},{1},'{2}','{3}','{4}')")
                cursor.execute(sql.format( clientes[0],clientes[1], clientes[2], clientes[3], clientes[4]))
                self.conexion.commit()
                print("Registro exitoso")
            except Error as ex:
                print("Error en el intento: {0}".format(ex))

    def eliminar(self,reserEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = (" delete from reservaciones where id ={0}")
                cursor.execute(sql.format(reserEliminar))
                self.conexion.commit()
                print("La reserva se ha eliminado")
            except Error as ex:
                print("Error en el intento: {0}".format(ex))
    def actualizar(self, clientesActualizar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update clientes set dni ={0}, nombre ='{1}', apellido ='{2}', direccion ='{3}' where id ={4} "
                cursor.execute(sql.format (clientesActualizar[1], clientesActualizar[2],clientesActualizar[3],clientesActualizar[4], clientesActualizar[0]))
                self.conexion.commit()
                print("Actualizado exitosamente")
            except Error as ex:
                print("Error en el intento de conectar; {0}".format(ex))
    def listarReser(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select * from reservaciones")
                respuesta = cursor.fetchall()
                return respuesta
            except Error as ex:

                print("Error en el intento de conectar: {0}".format(ex)) 
          
    def registroReser (self, reservaciones):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("insert into reservaciones( id, Hora, Fecha, cantidadmesa, id_clientes ) values ({0},'{1}','{2}',{3},{4})")
                cursor.execute(sql.format( reservaciones[0],reservaciones[1], reservaciones[2], reservaciones[3], reservaciones[4]))
                self.conexion.commit()
                print("Registro exitoso")
            except Error as ex:
                print("Error en el intento: {0}".format(ex))

    def actualizarReser(self, reservacionesActualizar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update reservaciones set Hora='{0}', Fecha='{1}', cantidadmesa={2}, id_clientes ={3} where id ={4} "
                cursor.execute(sql.format (reservacionesActualizar[1], reservacionesActualizar[2],reservacionesActualizar[3],reservacionesActualizar[4], reservacionesActualizar[0]))
                self.conexion.commit()
                print("Actualizado exitosamente")
            except Error as ex:
                print("Error en el intento de conectar; {0}".format(ex))

  


        



           

        