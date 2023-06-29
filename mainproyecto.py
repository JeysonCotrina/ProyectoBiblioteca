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
    print('|        OPCIONES DE ENCARGADO      |')
    print('°-----------------------------------°')
    print('| 1)Ver Informacion de los clientes |')
    print('| 2)Realizar Prestamo               |')
    print('| 3)Modificar stock                 |')
    print('| 4)Listado de Prestamos            |')
    print('°-----------------------------------°')

def MenuDocente():
    print('°-----------------------------------°')
    print('|         OPCIONES DOCENTE          |')
    print('°-----------------------------------°')
    print('| 1)Solicitar Prestamo              |')
    print('| 2)Listado de Libros Prestados     |')
    print('| 3)Ver multas                      |')
    print('°-----------------------------------°')

def MenuAlumno():
    print('°-----------------------------------°')
    print('|          OPCIONES DOCENTE         |')
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
            if(len(r) == 1):
                    MenuEncargado()
                    op=int(input('Eliga la opcion que desea realizar: '))
                    if op == 1:
                        print('INFORMACIÓN DE CLIENTES')
                        rut=input('RUN de cliente a buscar: ')
                        r=biblio.InfoCliente(rut)
                        q,w,e,h,t,l, =r
                        print('-----------Datos del Cliente--------------')
                        print(f'Nombres: {q}\nApellido: {w}\nTelefono: {e}\nCorreo: {h}\nTipo Cliente: {"Docente" if t == 1 else "Estudiante"}\nMultas: ${l}')
                        print('------------------------------------------')
                        
                    elif op == 2:
                        print('Realizar Prestamo')
                    elif op == 3:
                        print('Modificar stock')
                    elif op == 4:
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
                            
                            
            else:
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
            if(len(r)==1):
                MenuAlumno()
                op=int(input('Eliga la opcion que desea realizar: '))

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
