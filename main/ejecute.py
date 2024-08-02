from clases.usuarios import Usuarios
from databases.conexion import connetion
import mysql.connector
print("********************* Bienvenido a su control de damas de compañia *********************")
print('''
    Ingrese:
    1) Registrarse
    2) Iniciar sesion
    ''')
option = int(input("Por favor ingrese una opcion: "))

if option == 1:
    new_user = Usuarios(None, None, None, None, None)
    new_user.register_user()
elif option == 2:
    validation = Usuarios(None,None,None,None,None)
    #validation.login_user()
    opcc = validation.login_user()
    if opcc == 1:
        validation.show_all_users()
    elif opcc == 2:
        validation.update_user()
    elif opcc == 3:
        validation.delete_user()
    else:
        print("ingreso exitoso")




