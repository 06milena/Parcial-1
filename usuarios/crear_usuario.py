from config.db import DB
import re


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
      print ("Registro Correctamente")
      cursor.close()
    


def crear():
      nombre= input('Ingrese el nombre: ')
      email = input('Ingrese el correo: ') 
      contrasena = input('Ingrese la contraseña: ')
      crearUsuario(nombre,email,contrasena)
      bandera=1

def validar_contraseña():
      contrasena = input('Ingrese la contraseña: ')
      while True:
        if len(contrasena)<8:
              print('contraseña de 8 caracteres')
        elif re.search('[0-9]',contrasena) is None:
              print('que tenga un numero')
        elif re.search('[A-Z]',contrasena) is None:
              print('que tenga una mayuscula')
        else:
              print('es correcto')
