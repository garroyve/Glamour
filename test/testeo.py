from clases.usuarios import Usuarios


def main():
    #Crear una instancia de Usuarios y registrar un usuario
    #nuevo_usuario = Usuarios(id_user= "", name_user="Nataly", last_name_user="Alzate", email="nat_alzate@hotmail.com", password="23232")
    #nuevo_usuario.register_user()

    # Mostramos usuarios
    print("******* Lista de Usuarios *********")
    Usuarios.show_all_users()

    # Eliminar usuario con referencia user_id
    delete_user = 12
    eliminar = Usuarios(id_user=delete_user, name_user=None, last_name_user=None, email=None, password=None)

    # Llama al método para eliminar el usuario
    eliminar.delete_user()

    print("******* Lista de Usuarios actualizada *********")
    Usuarios.show_all_users()

if __name__ == "__main__":
    main()

"""nuevo_usuario = Usuarios(name_user = "Nicolas", last_name_user = "Godoy", email = "nio202gmail.com", password= 456)

nuevo_usuario.register_user() """