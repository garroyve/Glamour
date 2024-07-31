from databases.conexion import connetion
import mysql.connector
class Servicios:

    def __init__(self, id_servicio=None, categoria=None):
        self._id_servicio = id_servicio
        self._categoria = categoria

    @property
    def id_servicio(self):
        return self._id_servicio

    @id_servicio.setter
    def id_servicio(self, value):
        self._id_servicio = value

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value


    #  ingresar un nuevo servicio
    def get_into_service(self):
        try:
            conn = self.connetion()
            if conn:
                cursor = conn.cursor()
                sql = """ INSERT INTO services (categoria)
                          VALUES (%s) """
                values = (self._categoria,)
                cursor.execute(sql, values)
                conn.commit()
                print("El servicio se ingresó correctamente con ID:", cursor.lastrowid)

        except mysql.connector.Error as error:
            print("Error al guardar el servicio:", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")

    # actualizar un servicio
    def update_service(self):
        try:
            conn = self.connection()
            if conn:
                cursor = conn.cursor()
                sql = """ UPDATE services
                          SET categoria = %s
                          WHERE id_servicio = %s """
                values = (self._categoria, self._id_servicio)
                cursor.execute(sql, values)
                conn.commit()
                if cursor.rowcount > 0:
                    print("El servicio se actualizó correctamente.")
                else:
                    print("No se encontró el servicio para actualizar.")

        except mysql.connector.Error as error:
            print("Error al actualizar el servicio:", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")

    # mostrar los detalles
    def show_service(self):
        try:
            conn = self.connection()
            if conn:
                cursor = conn.cursor()
                sql = """ SELECT categoria FROM services WHERE id_servicio = %s """
                values = (self._id_servicio,)
                cursor.execute(sql, values)
                result = cursor.fetchone()

                if result:
                    print(f"Categoría: {result[0]}")
                else:
                    print("No se encontró el servicio con el ID proporcionado.")

        except mysql.connector.Error as error:
            print("Error al obtener los datos del servicio:", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")

    # Meliminar un servicio
    def delete_service(self):
        try:
            conn = self.connection()
            if conn:
                cursor = conn.cursor()
                sql = """ DELETE FROM services WHERE id_servicio = %s """
                values = (self._id_servicio,)
                cursor.execute(sql, values)
                conn.commit()

                if cursor.rowcount > 0:
                    print("El servicio se eliminó correctamente.")
                else:
                    print("No se encontró el servicio para eliminar.")

        except mysql.connector.Error as error:
            print("Error al eliminar el servicio:", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")