from metodo import Metodos
from conectorbd import Conectar

def menu():
    continuar = True
    while continuar:
        correcta = False
        while not correcta:
            print(''' 
                        \n 1-Listado de clientes \n 
                        \n 2-Registrar \n 
                        \n 3-Modificar Registro \n 
                        \n 4-Listar Reservacion \n 
                        \n 5-Registrar Reservaciones \n
                        \n 6-Modificar Reservaciones \n 
                        \n 7-Eliminar Reservaciones \n 
                        \n 8-Salir del Programa \n''' )

            opcion = int(input("\n Ingrese una opcion: \n"))
            if opcion < 1 and opcion > 7:
                print("\n Opcion invalida \n")
            elif opcion == 8 :
                continuar = False
                print("\n Fin de los ingresos. Gracias \n")
                break
            else:

                correcta = True
                opciones(opcion)

def opciones (opcion):
    conectar = Conectar()
    metodos = Metodos()



    if opcion == 1 :
        try:
            clientes = conectar.listar()
            if len (clientes) > 0:
                metodos.listarClientes(clientes)
            else:
                print ("\n No se encontraron registros\n")
        except:
            print ("Ocurrio un error")

    elif opcion == 2:
        
        clientes = metodos.registrarClientes()
        try:
            conectar.registro(clientes)
        except:
            print("\n Ocurrio un error \n")
    elif opcion == 7:
        try:
            clientes = conectar.listarReser()
            if len(clientes) > 0:
                ideliminar = metodos.eliminarReser(clientes)
                if not ideliminar == '':
                    conectar.eliminar(ideliminar)
                else:
                    print("\n No se encontro el registro solicitado \n")
            else:
                print("\n No se encontraron registros \n")
        except:
            print("\n Ocurrio un error en el intento de eliminacion \n") 

    elif opcion == 3:
        try:
            clientes = conectar.listar()
            if len(clientes) > 0:
                idActualizar = metodos.actualizarClientes(clientes)
                if idActualizar:
                    conectar.actualizar(idActualizar)
                else:
                    print("No se encontro el registro solicitado")
            else:
                print("No se encontraron registros")
        except:
            print("Ocurrio un error")  

                

    if opcion == 4 :
        try:
            reservas = conectar.listarReser()
            if len (reservas) > 0:
                metodos.listarReservas(reservas)
            else:
                print ("No se encontraron registros")
        except:
            print ("Ocurrio un error")


    elif opcion == 5:
                    
        clientes = metodos.registrarReservaciones()


                    
        try:
                        
                        
            conectar.registroReser(clientes)
        except:
            print("Ocurrio un error")



   
    elif opcion == 6:
        try:
            reservaciones = conectar.listarReser()
            if len(reservaciones) > 0:
                idActualizar = metodos.modificarReservaciones(reservaciones)
                if idActualizar:
                    conectar.actualizarReser(idActualizar)
                else:
                    print("No se encontro el registro solicitado")
            else:
                print("No se encontraron registros")
        except:
            print("Ocurrio un error") 
        
menu()

                


         
    



