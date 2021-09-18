from config.db import DB


def crearUsuario(nombre, email, contrasena):
      cursor = DB.cursor()
      cursor.execute('''insert into 
        usuarios(nombre, email, contrasena)
        values(%s, %s, %s)''', (
          nombre,
          email,
          contrasena,
        ))
      DB.commit()
      print ("Registro Grabado  Correctamente")
      cursor.close()
    


def crear():
      nombre= input('Ingrese el nombre: ')
      email = input('Ingrese el correo: ')
      contrasena = input('Ingrese la contraseña: ')
      crearUsuario(nombre,email,contrasena)
      bandera=1
