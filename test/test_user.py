from clases.usuarios import Usuarios
from databases.conexion import connetion

''' CREAMOS USUARIOS '''
#new_user = Usuarios(None, None, None, None, None)
#new_user.register_user()


''' MOSTRAMOS USUARIOS REGISTRADOS '''
#Usuarios.show_all_users()

''' ELIMINAMOS USER CON REFERENCIA ID '''
#eliminar = Usuarios(None, None,None, None, None)
#eliminar.delete_user()
#Usuarios.show_all_users()

''' MODIFICAR USUARIO '''
#Usuarios.show_all_users()
#modificar = Usuarios(None, None, None, None, None)
#modificar.update_user()
#Usuarios.show_all_users()

''' LOGIN '''

logui = Usuarios(None,None,None,None,None)
logui.login_user()
