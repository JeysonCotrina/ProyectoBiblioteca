from proyecto import Biblioteca
biblio = Biblioteca()

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
    print('| 4)Modificar Catalogo              |')
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
    print('|          LOGIN DOCENTE            |')
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
            rut=input('Ingrese su rut: ')
            contrasena=input('Ingrese su Contraseña: ')
            r=biblio.identificar_usuario(rut,contrasena)
            if(len(r) == 1):
                inicioUsuario ='si'
                while inicioUsuario=='si': 
                    MenuEncargado()
                    op=int(input('Eliga la opcion que desea realizar: '))
                    if op == 1:
                        print('opcion 1')
                    elif op == 2:
                        print('opcion 2')
                    elif op == 3:
                        print('opcion 3')
                    elif op == 4:
                        print('opcion 4')
                    elif op == 5:
                        print('opcion 5')
                    else:
                        print('----------------WARNING------------------')
                        print('     La opción elegida no es valida. Eliga una de las siguientes:      ')
                        print('        1) Volver a opciones \n        2) Cerrar Sesión')
                        se=int(input('---> '))
                        if se == 1:
                            inicioUsuario = 'si'
                        elif se >= 2:
                            print('*****Vuelva pronto a la biblioteca*****')
                        break
            else:
                print('----------------WARNING------------------')
                print('Compruebe sus datos y vuelva a ingresarlo')
        elif el==2:
            print('----IDENTIFIQUESE----')
            rut=input('Ingrese su rut: ')
            contrasena=input('Ingrese su Contraseña: ')
            r=biblio.identificar_docente(rut,contrasena)
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
            r=biblio.identificar_alumno(rut,contrasena)
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
                


if __name__ == '__main__':
    main() 
