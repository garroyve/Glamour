from clases.usuarios import Usuarios
from clases.employee import Employees
from clases.servicios import Servicios


def main():
    #------------------------ Creamos usuario ----------------------------#
    #nuevo_usuario = Usuarios(id_user= "", name_user="Nataly", last_name_user="Alzate", email="nat_alzate@hotmail.com", password="23232") #Crear una instancia de Usuarios y registrar un usuario
    #nuevo_usuario.register_user() # lo agregamos con el metodo

    #----------------------- Mostramos usuarios --------------------#
    print("******* Lista de Usuarios *********")
    Usuarios.show_all_users()
    #---------------------------------------------------------------#

    #------------------ Eliminar usuario con referencia user_id------------------#
    delete_user = 12
    eliminar = Usuarios(id_user=delete_user, name_user=None, last_name_user=None, email=None, password=None) # Instancia para eliminar usuario
    eliminar.delete_user() # Llama al método para eliminar el usuario
    #----------------------------------------------------------------------------#

    #----------------- Crear una instancia del usuario con un id existente --------------------#
    usuario = Usuarios(id_user=15, name_user=None, last_name_user=None, email=None, password=None)# creamos la instancia
    usuario.update_user('name_user', 'Johnny')# Actualizar el nombre del usuario
    usuario.update_user('email', 'johnny.doe@hahss.com')# Actualizar el correo electrónico del usuario
    usuario.update_user('last_name_user', 'arboleda')
    #--------------------------------------------------------------------------------------------#

    #------------------ Lista actualizada -------------------------------------------------------#
    print("******* Lista de Usuarios actualizada *********")
    Usuarios.show_all_users()

    #_________________ ingresando aun empleado__________________________
    print('__________aca estamos ingresando un empleados__________')

    #nicolas = Employees(None, 'nicol', 'mendez', 'colombiana', 23, 'f', 500000)
    #nicolas.get_into_employee()
    ni = Employees(2,None,None,None,None,None,None)
    ni.delete_employee()
if __name__ == "__main__":
    main()

"""nuevo_usuario = Usuarios(name_user = "Nicolas", last_name_user = "Godoy", email = "nio202gmail.com", password= 456)

nuevo_usuario.register_user() """