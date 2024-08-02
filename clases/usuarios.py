from databases.conexion import connetion
import mysql.connector

class Usuarios:
    id_user = None
    name_user = None
    last_name_user = None
    email = None
    password = None
    def __init__(self,id_user, name_user, last_name_user, email, password):
        self._id_user = id_user
        self._name_user = name_user
        self._last_name_user = last_name_user
        self._email = email
        self._password = password

        '''metodo Getter'''

    @property
    def id_user(self):
        return self._id_user

    @property
    def name_user(self):
        return self._name_user

    @property
    def last_name_user(self):
        return self._last_name_user

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

        '''metodo Setter'''


    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @name_user.setter
    def name_user(self, name_user):
        self._name_user = name_user

    @last_name_user.setter
    def last_name_user(self, last_name_user):
        self._last_name_user = last_name_user

    @email.setter
    def email(self, email):
        self._email = email

    @password.setter
    def password(self, password):
        self._password = password

    def register_user(self):
        try:
            db = connetion()
            if db:
                cursor = db.cursor() # cursor para crear consultas
                #self._id_user = int(input("ID: "))
                self._name_user = input("Nombre: ")
                self._last_name_user = input("Apellido: ")
                self._email = input("Correo: ")
                self._password = input("Contraseña: ")
                query = "INSERT INTO users (name_user, last_name_user, email, password) VALUES (%s, %s, %s, %s)"
                values = (self._name_user, self._last_name_user, self._email, self._password)
                cursor.execute(query, values)
                db.commit()

                print("Usuario creado exitosamente")

        except mysql.connector.Error as error:
            print("Error al insertar el usuario ", error)
        finally:
            if db:
                cursor.close()
                db.close()
                print("Conexion cerrada ")
    @staticmethod
    def show_all_users():
        try:
            db = connetion()
            if db:
                cursor = db.cursor()

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
            if db:
                db.close()
                db.close()
                print("Conexion cerrada")

    def delete_user(self):

        try:
            db = connetion()
            if db:
                cursor = db.cursor()
                self._id_user = input("Ingrese el id del usuario que desea eliminar:  ")
                query = "DELETE FROM users WHERE id_user = %s"
                value = (self._id_user,)
                cursor.execute(query, value)
                db.commit()
                if cursor.rowcount > 0:
                    print("Usuario eliminado exitosamente")
                else:
                    print("No se encontró un usuario con el ID proporcionado")
        except mysql.connector.Error as error:
            print("Error al eliminar el usuario: ", error)
        finally:
            if db:
                cursor.close()
                db.close()
                print("Conexión cerrada")
                print("todo salio bien")

    def update_user(self):
        try:
            db = connetion()
            if db:
                cursor = db.cursor(dictionary=True)

                self._id_user = input("Introduce el ID del usuario que deseas actualizar: ").strip()

                # Obtiene la información actual del usuario
                cursor.execute("SELECT * FROM users WHERE id_user = %s", (self.id_user,))
                user_info = cursor.fetchone()

                if not user_info:
                    print("No se encontró un usuario con el ID proporcionado.")
                    return

                print("Información actual del usuario:")
                for key, value in user_info.items():
                    print(f"{key}: {value}")

                # Solicita el campo a actualizar
                field = input("¿Qué campo deseas actualizar? (name_user, last_name_user, email, password): ").strip()

                # Diccionario para mapear los nombres de los campos con sus nombres en la base de datos
                field_map = {
                    'name_user': 'name_user',
                    'last_name_user': 'last_name_user',
                    'email': 'email',
                    'password': 'password'
                }

                # Verifica que el campo sea válido
                if field not in field_map:
                    print("Campo no válido")
                    return

                value = input(f"Introduce el nuevo valor para {field}: ").strip()

                # Construye y ejecuta la consulta SQL
                query = f"UPDATE users SET {field_map[field]} = %s WHERE id_user = %s"
                cursor.execute(query, (value, self.id_user))
                db.commit()

                if cursor.rowcount > 0:
                    print("Usuario actualizado exitosamente")
                else:
                    print("No se encontró un usuario con el ID proporcionado o no se realizaron cambios")

        except mysql.connector.Error as error:
            print("Error al actualizar el usuario: ", error)
        finally:
            if db:
                cursor.close()
                db.close()
                print("Conexión cerrada")
