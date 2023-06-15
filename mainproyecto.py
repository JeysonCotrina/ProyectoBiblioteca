from proyecto import Biblioteca
biblio = Biblioteca()

def main():
    print(')---------------------------------(')
    print(')    Login de Indentificacion     (')
    print(')---------------------------------(')
    print(')          1)Encargado            (')
    print(')          2)Docente              (')
    print(')          3)Estudiante           (')
    print(')---------------------------------(')
    el=int(input('Eliga una opcion: '))
    if el==1:
        print('----IDENTIFIQUESE----')
        rut=input('Ingrese su rut: ')
        contrasena=input('Contrasena: ')
        r=biblio.identificar_usuario(rut,contrasena)
        if(len(r)==1):
            print('Login Exitoso')
        else:
            print('----------------WARNING------------------')
            print('Compruebe sus datos y vuelva a ingresarlo')
    elif el==2:
        rut=input('Ingrese su rut: ')
        contrasena=input('Contrasena: ')
        r=biblio.identificar_docente(rut,contrasena)
        if(len(r)==1):
            print('Login Exitoso')
        else:
            print('----------------WARNING------------------')
            print('Compruebe sus datos y vuelva a ingresarlo')
    elif el==3:
        print('ELIGISTE ESTUDIANTE')
        rut=input('Ingrese su rut: ')
        contrasena=input('Contrasena: ')
        r=biblio.identificar_alumno(rut,contrasena)
        if(len(r)==1):
            print('Login Exitoso')
        else:
            print('----------------WARNING------------------')
            print('Compruebe sus datos y vuelva a ingresarlo')
    else:
        print('No se encuentra esa opción')


if __name__ == '__main__':
    main() 
