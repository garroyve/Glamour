from databases.conexion import connetion
import mysql.connector
class Employees:

    def __init__(self, id_employee, name_employee, last_name_employee, nationality, age, sex, price):
        self._id_employee = id_employee
        self._name_employee = name_employee
        self._last_name_employee = last_name_employee
        self._nationality = nationality
        self._age = age
        self._sex = sex
        self._price = price

    @property
    def id_employee(self):
        return self._id_employee

    @id_employee.setter
    def id_employee(self, value):
        self._id_employee = value

    @property
    def name_employee(self):
        return self._name_employee

    @name_employee.setter
    def name_employee(self, value):
        self._name_employee = value

    @property
    def last_name_employee(self):
        return self._last_name_employee

    @last_name_employee.setter
    def last_name_employee(self, value):
        self._last_name_employee = value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 18:
            raise ValueError(" Que sea mayor de 18")
        self._age = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if value not in ['M', 'F', 'T']:
            raise ValueError(" Son:  'M', 'F', or 'T'")
        self._sex = value

    @property
    def price(self):
        return self._price

    @price.setter
    def preci(self, value):
        if value < 50000:
            raise ValueError("Que sea mayor a 50.000")
        self._price = value


    # ingresar
    def get_into_employee(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                sql = """ INSERT INTO employees (name_employee, last_name_employee, nationality, age, sex, price)
                         VALUES 
                         (%s, %s, %s, %s, %s, %s) """
                values = (self._name_employee, self._last_name_employee, self._nationality, self._age, self._sex, self._price)
                cursor.execute(sql, values)
                conn.commit()
                print("El empleado se ingreso correctamente")

        except mysql.connector.Error as error:
            print("Erro al guardar el empleado {}".format(error))
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("conexion cerrada")

    # actualizar
    def update_employee(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                sql = """
                        UPDATE employees
                        SET name_employee = %s,
                            last_name_employee = %s,
                            nationality = %s,
                            age = %s,
                            sex = %s,
                            prince = %s
                        WHERE id_employee = %s
                        """
                values = (self._id_employee, self._name_employee, self._last_name_employee, self._nationality, self._age, self._sex, self._price)
                cursor.execute(sql, values)
                conn.commit()
                if cursor.rowcount > 0:
                    print("El empleado se actualizo correctamente")
                else:
                    print("No se encontro el empleado para actualizar")

        except mysql.connector.Error as error:
            print("Error al actualizar el empleado: {}".format(error))
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexion cerrada")

    # mostrar empleado
    def show_employee(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                sql = "SELECT name_employee, last_name_employe, nationality, age, sex, price FROM employees WHERE id_employe = %s"
                values = (self._id_employee,)
                cursor.execute(sql, values)
                result = cursor.fetchone()

                if result:
                    name_employee, last_name_employee, nationality, age, sex, price = result
                    print(f"Nombre: {name_employee}")
                    print(f"Apellid: {last_name_employee}")
                    print(f"Nacionalidad: {nationality}")
                    print(f"Edad: {age}")
                    print(f"Genero: {sex}")
                    print(f"Precio: {price}")
                else:
                    print("No se encontro el empleado con el id proporcionado")

        except mysql.connector.Error as error:
            print("Error al obtener los datos del empleado: {}".format(error))
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Coexion cerrada")

    # eliminar
    def delete_employee(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                sql = "DELETE FROM employees WHERE id_employee = %s"
                values = (self._id_employee,)
                cursor.execute(sql, values)
                conn.commit()

                if cursor.rowcount > 0:
                    print("EL empleado se elimino correctamente")
                else:
                    print("No se encontro el empleado para eliminar")

        except mysql.connector.Error as error:
            print("Error al eliminar el empleado: {}".format(error))
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexion cerrada")