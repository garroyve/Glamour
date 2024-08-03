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

        self._age = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):

        self._sex = value

    @property
    def price(self):
        return self._price

    @price.setter
    def preci(self, value):

        self._price = value

    import mysql.connector



    def get_employee_data(self):
        self._name_employee = input("Ingrese el nombre del empleado: ")
        self._last_name_employee = input("Ingrese el apellido del empleado: ")
        self._nationality = input("Ingrese la nacionalidad del empleado: ")
        self._age = int(input("Ingrese la edad del empleado: "))
        self._sex = input("Ingrese el género del empleado: ")
        self._price = float(input("Ingrese el precio del empleado: "))
    def get_into_employee(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                sql = """ INSERT INTO employees (name_employee, last_name_employee, nationality, age, sex, price)
                         VALUES 
                         (%s, %s, %s, %s, %s, %s) """
                self.get_employee_data()
                values = (
                self._name_employee, self._last_name_employee, self._nationality, self._age, self._sex, self._price)
                cursor.execute(sql, values)
                conn.commit()
                print("El empleado se ingresó correctamente")
        except mysql.connector.Error as error:
            print(f"Error al guardar el empleado: {error}")
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")
    def update_employee(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                self._id_employee = int(input("Ingrese el ID del empleado a actualizar: "))
                self.get_employee_data()
                sql = """
                        UPDATE employees
                        SET name_employee = %s,
                            last_name_employee = %s,
                            nationality = %s,
                            age = %s,
                            sex = %s,
                            price = %s
                        WHERE id_employee = %s
                        """
                values = (
                self._name_employee, self._last_name_employee, self._nationality, self._age, self._sex, self._price,
                self._id_employee)
                cursor.execute(sql, values)
                conn.commit()
                if cursor.rowcount > 0:
                    print("El empleado se actualizó correctamente")
                else:
                    print("No se encontró el empleado para actualizar")
        except mysql.connector.Error as error:
            print(f"Error al actualizar el empleado: {error}")
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")
    def show_employee(self):
        try:
            db = connetion()
            if db:
                cursor = db.cursor()

                query = "SELECT id_employee, name_employee, last_name_employee, nationality,age,sex,price FROM employees"
                cursor.execute(query)
                users = cursor.fetchall()
                if users:
                    for user in users:
                        print(f"ID: {user[0]}, Nombre: {user[1]}, Apellido: {user[2]}, nacionalidad: {user[3]},edad: {user[4]},sexo: {user[5]},precio: {user[6]}")
                    else:
                        print("No hay usuarios en la base de datos. ")
        except mysql.connector.Error as error:
            print("Error al consultar usuarios: ", error)
        finally:
            if db:
                db.close()
                db.close()
                print("Conexion cerrada")
    def delete_employee(self):
        try:
            conn = connetion()
            if conn:
                cursor = conn.cursor()
                self._id_employee = int(input("Ingrese el ID del empleado a eliminar: "))
                sql = "DELETE FROM employees WHERE id_employee = %s"
                values = (self._id_employee,)
                cursor.execute(sql, values)
                conn.commit()
                if cursor.rowcount > 0:
                    print("El empleado se eliminó correctamente")
                else:
                    print("No se encontró el empleado para eliminar")
        except mysql.connector.Error as error:
            print(f"Error al eliminar el empleado: {error}")
        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexión cerrada")