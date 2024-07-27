import mysql.connector

def connetion():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            user = "root",
            password="",
            database = "users_glamour"


        )
        return conn
    except mysql.connector.Error as error:
        print("Error de conexion a la base de datos : ", error)
        return None

conn = connetion()


'''if conn is not None:
    print("Conexion exitosa")'''

