class Metodos():
    def listarClientes(self, clientes):
        contador = 1
        for alu in clientes:
            resultado = "{}-- ID {} DNI: {} Nombre: {} Apellido: {} Direccion: {} "
            print(resultado.format(contador,alu[0], alu[1], alu[2], alu[3], alu[4]))
            contador += 1

    def registrarClientes(self):
        print("\nRegistro de usuarios\n")

        id= int(input("Ingrese el Id: "))

        dniCorrecto = False
        while (not dniCorrecto):
            dni = input ("Ingrese el DNI: ")
            if len(dni) == 8 and dni.isnumeric():
                dniCorrecto = True
            else:
                print("El DNI debe contener 8 digitos")

        nombreCorrecto = False
        while ( not nombreCorrecto):
            nombre = str(input("Ingrese el nombre: ")).title()
            if len (nombre)> 2:
                if nombre.istitle():
                    if nombre.isalpha():
                        nombreCorrecto = True
                    else:
                        print("El nombre no puede tener numeros")
                else:
                    print("Debe ingresar la primera letra con mayusculas")
            else:
                print("El  nombre debe tener minimo 3 caracteres")

        apellido = str(input("Ingrese el apellido: ")).title()

        direccion = str(input("Ingrese la direccion: "))

        clientes = ( id, dni, nombre, apellido, direccion)

        return clientes

    def eliminarReser(self, reservacion):
        existeId = False
        idEliminar = int(input("Ingrese el Id de la reserva a eliminar: "))
        for re in reservacion:
            if re[0] == idEliminar:
                existeId = True
                break
        if not idEliminar:
            lidEliminar = ''
        return idEliminar

    def actualizarClientes(self, clientes):
        existeId = False
        idActualizar = int(input("Ingrese el numero ID a actualizar: "))
        for alu in clientes:
            if alu[0] == idActualizar:
                existeId = True
                break
        if existeId:

            
            dni = input("Ingrese su DNI: ")
            nombreCorrecto = False
            while(not nombreCorrecto):
                nombre = str(input("Ingrese el nombre: ")).title()
                if len(nombre)> 2 :
                    if nombre.istitle():
                        if nombre.isalpha():
                            nombreCorrecto = True
                        else:
                          print("El nombre no puede contener numeros")
                    else:
                        print("Debe ingresar el primer caracter en mayusculas")
                else:
                    print("El nombre debe tener minimo tres caracteres")

            apellido = str(input("Ingrese el apelllido: ")).title()
            direccion = str(input("Ingrese direccion: "))
            clientes = (idActualizar, dni, nombre, apellido, direccion)

        else:
            clientes = None
        return clientes   
    def listarReservas(self, reservacion):
        contador = 1
        for re in reservacion:
            resultado = "{}-- ID {} Hora: {} Fecha: {} Cantidad: {} Cliente: {} "
            print(resultado.format( contador, re[0], re[1], re[2], re[3], re[4]))
            contador += 1


    def registrarReservaciones(self):
      print("\nRegistro de usuarios\n")

      id= int(input("Ingrese el Id: "))
      Hora = input("Ingrese hora en este formato: 00:00:00: ")
      Fecha = input("Ingrese fecha en el siguiente formato: AAAA-MM-DD: ")
      cantidadmesa = int(input("Ingrese cantidad de personas: "))
      id_clientes= int(input("Ingrese Identificador del cliente: "))

      reservacion = (id, Hora, Fecha, cantidadmesa, id_clientes)
      #reservacion = None
      return reservacion  

    def modificarReservaciones(self, reservaciones):
        existeId = False
        idActualizar = int(input("Ingrese el numero ID a actualizar: "))
        for re in reservaciones:
            if re[0] == idActualizar:

                existeId = True
                break
        if existeId:

            Hora = input("Ingrese el Hora con formato oo:oo:oo : ")
            Fecha = str(input("Ingrese Fecha en formato AAAA-MM-DD : "))
            cantidadmesa = int(input("Ingrese Cantidad de personas: "))
            id_clientes = int(input("Ingrese Id Clientes: "))


            clientes = (idActualizar, Hora, Fecha, cantidadmesa , id_clientes)

        else:
            clientes = None
        return clientes                 
