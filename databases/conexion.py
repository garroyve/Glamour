import mysql.connector

def connetion():
    try:
        db = mysql.connector.connect(
            host="localhost",
            port="3306",
            user = "root",
            password="",
            database = "users_glamour"


        )
        return db
    except mysql.connector.Error as error:
        print("Error de conexion a la base de datos : ", error)
        return None

db = connetion()

''' if db is not None:
    print("Conexion exitosa") '''


