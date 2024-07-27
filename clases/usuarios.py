from databases.conexion import connetion
import mysql.connector


class Usuarios:

    def __init__(self, id_user, name_user, last_name_user, email, password):
        self.__id_user = id_user
        self.__name_user = name_user
        self.__last_name_user = last_name_user
        self.__email = email
        self.__password = password

        '''metodo Getter'''

    def get_id_user(self):
        return self.__id_user

    def get_name_user(self):
        return self.__name_user

    def get_last_name_user(self):
        return self.__last_name_user

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

        '''metodo Setter'''

    def set_id_user(self, id_user):
        self.__id_user = id_user

    def set_name_user(self, name_user):
        self.__name_user = name_user

    def set_last_name_user(self, last_name_user):
        self.__last_name_user = last_name_user

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def register_user(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor() # cursor para crear consultas

                sql = "INSERT INTO users (name_user, last_name_user, email, password) VALUES (%s, %s, %s, %s)"
                values = (self.__name_user, self.__last_name_user, self.__email, self.__password)
                cursor.execute(sql, values)
                conn.commit()

                print("Usuario creado exitosamente")

        except mysql.connector.Error as error:
            print("Error al insertar el usuario ", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexion cerrada ")
    @staticmethod
    def show_all_users():
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()

                query = "SELECT id_user, name_user, last_name_user, email FROM users"
                cursor.execute(query)
                users = cursor.fetchall()
                if users:
                    for user in users:
                        print(f"ID: {user[0]}, Nombre: {user[1]}, Apellido: {user[2]}, Email: {user[3]}")
                    else:
                        print("No hay usuarios en la base de datos. ")
        except mysql.connector.Error as error:
            print("Error al consultar usuarios: ", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexion cerrada")

    def delete_user(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                sql = "DELETE FROM users WHERE id_user = %s"
                value = (self.__id_user,)
                cursor.execute(sql, value)
                conn.commit()
                if cursor.rowcount > 0:
                    print("Usuario eliminado exitosamente")
                else:
                    print("No se encontró un usuario con el ID proporcionado")
        except mysql.connector.Error as error:
            print("Error al eliminar el usuario: ", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")
                print("todo salio bien")