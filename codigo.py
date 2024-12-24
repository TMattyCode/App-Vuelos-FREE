nombres=[]
ruts=[]
telefonos=[]
bancos=[]
estado=[]
asientos=range(1,43)
for i in range(len(asientos)):#se agregan los espacios definidos a cada una de las listas
    nombres.append("")
    ruts.append("")
    telefonos.append("")
    bancos.append("")
    estado.append("disponible")#en la lista estado se agrega la palabra disponible
def Ocupado(asiento):
    ocupado=False
    contar=0
    for i in range(len(asientos)):#se hace un for con el rango de numero de asientos
        if asiento==asientos[i]:#se compara la variable asiento con los numeros de la lista asientos
            if estado[i]=="ocupado":#se pregunta si en esa posicion el estado es ocupado
                contar=contar+1
    if contar==1 or asiento>42:#se pregunta si el contar encontro un ocupado o el asiento es mayor a 42
        ocupado=True
    return ocupado#valor boolean
def Pagar(asiento,banco):
    valorTotal=0
    if asiento>=25 and asiento<=35:#se pregunta si el asiento esta entre los numeros 25 y 35 los cuales son asientos vip
        valor=240000
        if banco=="bancoUmayor":#si el banco es igual a bancoUmayor se le hace un descuernto del 15%
            descuento=(valor*15)/100
            valorTotal=valor-descuento
        else:
            valorTotal=valor
    else:#si no esta en ese rango
        valor=78900
        if banco=="bancoUmayor":#se le hace un descuento del 15%
            descuento=(valor*15)/100
            valorTotal=valor-descuento
        else:
            valorTotal=valor
    return valorTotal#valor int
def AsignarVuelo(nombre,rut,telefono,banco,asiento):
    for i in range(len(asientos)):
        if asiento==asientos[i]:
            nombres.pop(i)
            nombres.insert(i,nombre)
            ruts.pop(i)
            ruts.insert(i,rut)
            telefonos.pop(i)
            telefonos.insert(i,telefono)
            bancos.pop(i)
            bancos.insert(i,banco)
            estado.pop(i)
            estado.insert(i,"ocupado")
def AsientosDisponibles():
    nuevaLista=[]
    for i in range(len(asientos)):
        if estado[i]=="ocupado":
            nuevaLista.append("x")
        else:
            nuevaLista.append(asientos[i])
    return nuevaLista

def EliminarVuelo(asiento):
    ocupado=0
    for i in range(len(asientos)):
        if asiento==asientos[i]:
            if estado[i]=="ocupado":
                nombres.pop(i)
                nombres.insert(i,"")
                ruts.pop(i)
                ruts.insert(i,"")
                telefonos.pop(i)
                telefonos.insert(i,"")
                bancos.pop(i)
                bancos.insert(i,"")
                estado.pop(i)
                estado.insert(i,"disponible")
                print("asiento anulado con exito")
            else:
                print("el asiento ya estaba disponible")
print("Vuelos-FREE\n1. Procesar Ventas por Internet\n2. Ver asientos disponibles\n3. Comprar asiento\n4. Anular vuelo\n5. Modificar datos de pasajero\n6. Salir")
opcion=""
while opcion!="6":
    opcion=input("elegir opcion: ")
    if opcion=="1":
        ocupados=[]
        archivo=open("vtaInternet.txt","r")
        for linea in archivo:
            ocupados.append(int(linea))
        archivo.close()
        ocupados.sort()
        for i in range(len(asientos)):
            for j in range(len(ocupados)):
                if asientos[i]==ocupados[j]:
                    estado.pop(i)
                    estado.insert(i,"ocupado")
        print("Se ingresaron correctamente las ventas")
    elif opcion=="2":
        contar1=0
        contar2=0
        for asiento in AsientosDisponibles():
            contar1=contar1+1
            contar2=contar2+1
            if contar1==3:
                print(asiento,end="\t\t")
                contar1=0
            else:
                print(asiento,end="\t")
            if contar2==6:
                print()
                contar2=0
        print()
    elif opcion=="3":
        nombre=input("Nombre: ")
        rut=input("Rut: ")
        telefono=input("Telefono: ")
        banco=input("Banco: ")
        asiento=int(input("Numero Asiento: "))
        if Ocupado(asiento):
            print("asiento no disponible")
        else:
            print("asiento disponible")
            pagado=False
            while pagado==False:
                print("total a pagar:",Pagar(asiento,banco))
                pagar=int(input("ingresar dinero: "))
                if pagar>Pagar(asiento,banco):
                    vuelto=pagar-Pagar(asiento,banco)
                    print("vuelto:",vuelto)
                    AsignarVuelo(nombre,rut,telefono,banco,asiento)
                    print("vuelo asignado\ngracias")
                    pagado=True
                elif pagar<Pagar(asiento,banco):
                    print("dinero insuficiente")
                elif pagar==0:
                    print("pago interrumpido")
                    pagado=True
                else:
                    AsignarVuelo(nombre,rut,telefono,banco,asiento)
                    print("vuelo asignado\ngracias")
                    pagado=True               
    elif opcion=="4":
        asiento=int(input("Ingrese numero de asiento: "))
        EliminarVuelo(asiento)
    elif opcion=="5":
        booleano=False
        rut=input("Ingrese rut: ")
        asiento=int(input("numero asiento: "))
        for i in range(len(asientos)):
            if asiento==asientos[i] and rut==ruts[i]:
                booleano=True
                print("1. Cambiar Nombre\n2. Cambiar Telefono\n3. Volver")
                opcion1=0
                while opcion1!=3:
                    opcion1=int(input("ingresar opcion para cambiar datos: "))
                    if opcion1==1:
                        nombres.pop(i)
                        nuevoNombre=input("Ingrese nuevo Nombre: ")
                        nombres.insert(i,nuevoNombre)
                        print("nombre se cambio correctamente")
                    elif opcion1==2:
                        telefonos.pop(i)
                        nuevoTelefono=input("Ingrese nuevo Telefono: ")
                        telefonos.insert(i,nuevoTelefono)
                        print("telefono se cambio correctamente")
        if booleano==False:
            print("datos Incorrectos")
    elif opcion=="6":
        print("¡Adios!")
    else:
        print("opcion no existe")
