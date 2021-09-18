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

    cursor.close()


def crear():
      bandera=1

      while  bandera!=0:
            if validar== True:
                  bandera=0


def validar():
    contrasena=input( ' ')
    validar=False
    long=len(contrasena)
    espacio=False
    mayuscula=False
    minuscula=False
    numeros=False
    y=contrasena.isalnum()
    correcto=True

    for carac in contrasena:
        if carac.isspace()==True:
            espacio=True
        if carac.isupper()== True:
            mayuscula=True
        if carac.islower()== True:
            minuscula=True
        if carac.isdigit()== True:
            numeros=True

    if espacio==True:
        validar=False
    else:
        validar=True

    if long <8  and validar==True:
        print("Mínimo 8 caracteres")
        validar=False

    if mayuscula == True and minuscula ==True and numeros == True and y == False and validar ==True:
       validar = True
    else:
       correcto=False

    if validar == True and correcto==False:
        print("La contraseña elegida no es segura")

    if validar == True and correcto ==True:
       return True