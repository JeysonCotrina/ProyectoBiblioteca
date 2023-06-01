from proyecto import Biblioteca

alianza = Biblioteca()

def main():
    op = 'si'
    while op == 'si':
        print('----IDENTIFIQUESE----')
        rut_usuario=input('Ingrese su rut: ')
        r=alianza.identificar(rut_usuario)
        if r == None:
            print('--------RUT NO REGISTRADO EN SISTEMA--------')
            op=input('¿Desea ingresar nuevamente su Rut? SI/NO: ').lower()
            if op != 'si':
                print('Hasta luego')
        elif r != None:
            e,t, =r
            if e == 1:
                print(f'----> Bienvenido docente:  {t} ')
                print('')
                print('+-------------------------------------+')
                print('|               Menú                  |')
                print('+-------------------------------------+')
                print('| 1) LISTADO DE LIBROS PRESTADOS      |')
                print('| 2) PRORROGA DE ENTREGA DE LIBRO     |')
                print('| 3) CATALOGO DE LIBROS               |')
                print('+-------------------------------------+')
                opp=int(input('Ingrese una opción: '))
                if opp == 1:
                    print('Opcion 1')
                    
                elif opp == 2:
                    print('Opcion 2')
                
                elif opp == 3:
                    print('opcion 3')
                    
                else:
                    print('********Opcion no valido********')
                    



            elif e == 2:
                print(f'------> Bienvenido Alumno: {t} ')
                print('')
                print('+-----------------------------------+')
                print('|              Menú                 |')
                print('+-----------------------------------+')
                print('| 1) LISTADO DE LIBROS PRESTADOS    |')
                print('| 2) PRORROGA DE ENTREGA DE LIBRO   |')
                print('| 3) CATALOGO DE LIBROS             |')
                print('+-----------------------------------+')
                opp=int(input('Ingrese una opción: '))
                if opp == 1:
                    print('Opcion 1')
                    
                elif opp == 2:
                    print('Opcion 2')
                
                elif opp == 3:
                    print('opcion 3')
                    
                else:
                    print('********Opcion no valido********')

            elif e == 3:    
                print(f'----> Bienvenido Encargado:  {t}')
                print('+-----------------------------------+')
                print('|               Menú                |')
                print('+-----------------------------------+')
                print('| 1) Información de usuarios        |')
                print('| 2) Ultimos libros en prestamo     |')
                print('| 3) Modificar stock                |')
                print('| 4) Modificar catalogo             |')
                print('+-----------------------------------+')
                opp=int(input('Ingrese una opción: '))
                if opp == 1:
                    print('Opcion 1')
                    
                elif opp == 2:
                    print('Opcion 2')
                
                elif opp == 3:
                    print('opcion 3')
                
                elif opp==4:
                    print('opción 4')

                else:
                    print('********Opcion no valido********')






if __name__ == '__main__':
    main() 