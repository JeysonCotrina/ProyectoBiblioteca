from proyecto import Biblioteca,Encargado,Docente,Alumno
biblio = Biblioteca()
alumno=Alumno()
docente=Docente()
encargado=Encargado()

def Menu():
    print('°---------------------------------°')
    print('|    Login de Indentificacion     |')
    print('°---------------------------------°')
    print('|          1)Encargado            |')
    print('|          2)Docente              |')
    print('|          3)Estudiante           |')
    print('°---------------------------------°')

def MenuEncargado():
    print('°-----------------------------------°')
    print('|        LOGIN DE ENCARGADO         |')
    print('°-----------------------------------°')
    print('| 1)Ver Informacion de los clientes |')
    print('| 2)Realizar Prestamo               |')
    print('| 3)Modificar stock                 |')
    print('| 4)Eliminar Libro                  |')
    print('| 5)Listado de Prestamos            |')
    print('°-----------------------------------°')

def MenuDocente():
    print('°-----------------------------------°')
    print('|          LOGIN DOCENTE            |')
    print('°-----------------------------------°')
    print('| 1)Solicitar Prestamo              |')
    print('| 2)Listado de Libros Prestados     |')
    print('| 3)Ver multas                      |')
    print('°-----------------------------------°')

def MenuAlumno():
    print('°-----------------------------------°')
    print('|          LOGIN ALUMNO             |')
    print('°-----------------------------------°')
    print('| 1)Solicitar Prestamo              |')
    print('| 2)Listado de Libros Prestados     |')
    print('| 3)Ver multas                      |')
    print('°-----------------------------------°')

def main():
    inicio='si'
    while inicio =='si': 
        Menu()
        el=int(input('Eliga una opción: '))
        if el==1:
            print('----IDENTIFIQUESE----')
            rut=input('Ingrese su RUN: ')
            contrasena=input('Ingrese su Contraseña: ')
            r=encargado.identificar_usuario(rut,contrasena)
            z,x, =r #Z id_usuario   X rut
            if r != None:
                inicioUsuario ='si'
                while inicioUsuario =='si': 
                    MenuEncargado()
                    op=int(input('Eliga la opcion que desea realizar: '))
                    if op == 1:
                        print('INFORMACIÓN DE CLIENTES')
                        busqueda = 'si'
                        while busqueda == 'si':
                            rut=input('RUN de cliente a buscar: ')
                            r=biblio.InfoCliente(rut)
                            q,w,e,h,t,l,p,v, =r
                            print('-----------Datos del Cliente--------------')
                            print(f'Nombres: {w}\nApellido: {e}\nTelefono: {h}\nCorreo: {t}\nTipo Cliente: {"Docente" if p == 1 else "Estudiante"}\nMultas: ${l}')
                            print('------------------------------------------')
                            po=input('¿Desea buscar otro cliente? SI/NO: ').lower()
                            if po == 'si':
                                busqueda = 'si'
                            if po != 'si':
                                break
                    elif op == 2:
                        print('REALIZAR PRESTAMO')
                        rut_cliente = input('Ingrese el rut del cliente: ')
                        p=biblio.InfoCliente(rut_cliente)
                        if p != None:
                            f,a,s,d,g,h,j,l, = p
                            if j == 1:
                                id_cliente = l
                                error = 'si'
                                while error == 'si':
                                    codigo=input('Ingrese el codigo del Libro: ').upper()
                                    o = biblio.ValidarPrestamo(id_cliente,codigo)
                                    if o != None:
                                        print('-------------------WARNING--------------------')
                                        print('EL CLIENTE NO PUEDE ADQUIRIR EL MISMO EJEMPLAR')
                                        er=input('¿Ingresar otro código de libro? SI/NO: ').lower()
                                        if er == 'si':
                                            error='si'
                                        elif er != 'si':
                                            break
                                    elif o == None:
                                        if h > 0:
                                            print('EL usuario se encuentra con multas pendientes:')
                                            print(f'Cantidad en multas: ${h}')
                                        elif h == 0:
                                            id_usuario = z
                                            print('Ingrese la fecha de hoy')
                                            dia=int(input('Dia (Números):'))
                                            mes=int(input('Mes (Números):'))
                                            año=int(input('Año (Números):'))
                                            fecha_prestamo = (f'{año}/{mes}/{dia}')
                                            
                            if j == 2:
                                print('Alumno')
                                #ALUMNO: maximo de 4 libros a prestamo (acumulativos)

                    elif op == 3:
                       
                        print('MODIFICACION DE STOCK LIBROS ')
                        codigo_libro = input("Ingrese el codigo del Libro:  ")
                        resultado = biblio.InfoLibro(codigo_libro) 

                        print("--------------- Informacion del Libro  -----------------")
                        q,w,e,h,t= resultado
                        print(f"Titulo: {q}\nCantidad de Ejemplar: {w}\nAutor: {e}\nEditorial: {h}\nCategoria:{t}  ")
                        biblio.ModificarStock(codigo_libro)
                        
                        print("--------------- Registro Actualizado Exitoso  -----------------")
                        print("---------------------------------------------------------------")
                        print("--------------- Detalle Del codigo del Libro Actualizado -----------------")

                        
                        resultado = biblio.InfoLibro(codigo_libro) 
                        q,w,e,h,t= resultado
                        print(f"Titulo: {q}\nCantidad de Ejemplar: {w}\nAutor: {e}\nEditorial: {h}\nCategoria:{t}  ")

                       

                    elif op == 4:
                        print('Eliminar Libro')
                        codigo_libro= input("Ingrese el Codigo del Libro :  ")
                        resultado = biblio.identificar_prestamo(codigo_libro)
                        if(len(resultado) == 1):
                            print("---------------------------------------------------------------")
                            print("--------------- No se puede eliminar Libro,  EL EJEMPLAR SE ENCUENTRA EN PRESTAMO -----------------")
                           
                            

                        else:
                            print("--------------- Libro Eliminado  -----------------")
                            biblio.EliminarLibro(codigo_libro)


                    elif op == 5:
                        print('Listado de Prestamos')
                    else:
                        print('----------------WARNING------------------')
                        print('     La opción elegida no es valida. Eliga una de las siguientes:      ')
                        print('        1) Volver a opciones \n        2) Cerrar Sesión')
                        se=int(input('---> '))
                        if se == 1:
                            inicioUsuario = 'si'
                        else:
                            print('*****Vuelva pronto a la biblioteca*****')                

            elif r == None:
                print('----------------WARNING------------------')
                print('Compruebe sus datos y vuelva a ingresarlo')
        elif el==2:
            print('----IDENTIFIQUESE----')
            rut=input('Ingrese su rut: ')
            contrasena=input('Ingrese su Contraseña: ')
            r=docente.identificar_docente(rut,contrasena)
            if(len(r)==1):
                MenuDocente()
                op=int(input('Eliga la opcion que desea realizar: '))

            else:
                print('----------------WARNING------------------')
                print('Compruebe sus datos y vuelva a ingresarlo')
        elif el==3:
            print('----IDENTIFIQUESE----')
            rut=input('Ingrese su rut: ')
            contrasena=input('Ingrese su Contraseña: ')
            r=alumno.identificar_alumno(rut,contrasena)
            if r != None:
                a,b,c, = r
                MenuAlumno()
                op=int(input('Eliga la opcion que desea realizar: '))
                if op == 3:
                    print("---------------------------------------")
                    print("               Ver Multas              ")
                    print(f"Tienes ${c} en multas a pagar")
                    print("\n")



            else:
                print('----------------WARNING------------------')
                print('Compruebe sus datos y vuelva a ingresarlo')
        else:
            print('No se encuentra esa opción')
            inicio=input('¿Desea continuar? Escriba si o no: ').lower()
            if inicio!='si':
                print('Vuelva pronto a la biblioteca')
                break
                


if __name__ == '__main__':
    main() 
                        
