from proyecto import Biblioteca
biblio = Biblioteca()

def Menu():
    print(')---------------------------------(')
    print(')    Login de Indentificacion     (')
    print(')---------------------------------(')
    print(')          1)Encargado            (')
    print(')          2)Docente              (')
    print(')          3)Estudiante           (')
    print(')---------------------------------(')

def MenuEncargado():
    print(')-----------------------------------(')
    print(')        LOGIN DE ENCARGADO         (')
    print(')-----------------------------------(')
    print(') 1)Ver Informacion de los clientes (')
    print(') 2)Realizar Prestamo               (')
    print(') 3)Modificar stock                 (')
    print(') 4)Modificar Catalogo              (')
    print(') 5)Listado de Prestamos            (')
    print(')-----------------------------------(')

def MenuDocente():
    print(')-----------------------------------(')
    print(')          LOGIN DOCENTE            (')
    print(')-----------------------------------(')
    print(') 1)Solicitar Prestamo              (')
    print(') 2)Listado de Libros Prestados     (')
    print(') 3)Ver multas                      (')
    print(')-----------------------------------(')

def MenuAlumno():
    print(')-----------------------------------(')
    print(')          LOGIN ALUMNO             (')
    print(')-----------------------------------(')
    print(') 1)Solicitar Prestamo              (')
    print(') 2)Listado de Libros Prestados     (')
    print(') 3)Ver multas                      (')
    print(')-----------------------------------(')

def main():
    Menu()
    el=int(input('Eliga una opción: '))
    if el==1:
        print('----IDENTIFIQUESE----')
        rut=input('Ingrese su rut: ')
        contrasena=input('Ingrese su Contraseña: ')
        r=biblio.identificar_usuario(rut,contrasena)
        if(len(r)==1):
            MenuEncargado()
            op=int(input('Eliga la opcion que desea realizar: '))
        else:
            print('----------------WARNING------------------')
            print('Compruebe sus datos y vuelva a ingresarlo')
    elif el==2:
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


if __name__ == '__main__':
    main() 
