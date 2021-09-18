
from usuarios.crear_usuario import crear




def menuPrincipal():
    opcion=1
    
    while opcion !=0:
        print('---------------------------------')
        print('    Menu')
        print('1. Registrar')
        print('2. Iniciar sesion')
        print('3. Salir')

        opcion = int(input('SELECCIONE UNA OPCION: '))

        if opcion==1:
            crear()
        elif opcion==2:
            email = input('Ingrese el correo: ')
            contrasena = input('Ingrese la contraseña: ')
        elif opcion==3:
            break
        else:
            print("Opcion invalida ")


menuPrincipal()