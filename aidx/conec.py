import mysql.connector
import datetime
from escan import obtener_direccion_ip

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="3.209.34.159",
            user="root",
            password="iu7r97xq4b3e94b",
            database="encuestadb"
        )
        self.mycursor = self.mydb.cursor()
        #print(self.mydb, "conexión creada con éxito")

    def insert_data(self, ip_equipo):  # Aquí recibo ip_equipo como argumento
        sql = "INSERT INTO infeccion (ID, equipo, fecha) VALUES (%s, %s, %s)"
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtiene la fecha y hora actual
        val = (None, ip_equipo, fecha_actual)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

        print(self.mycursor.rowcount, "datos insertados con éxito.")
