import mysql.connector as conector
from app import *

# Conectamos con nuestra bases de datos.
def conectar_bbdd():

    base_de_dato = conector.connect(host="Localhost", port="3306", user="root", password="77046754", database="bicicletas", autocommit = "True")

    return base_de_dato

def consultar_bicicletas():

    #Crear una conexión.
    conexion = conectar_bbdd()

    #Creamos un cursor
    cursor = conexion.cursor()

    #Realizamos un scripts para consultas.
    sql_script = "SELECT + from bicicletas"

    cursor.execute(sql_script)

 #Cerramos conexión
def cerrar_conexion(conexion):

    conexion.close()

def insertar_bicicletas():
    #Creamos variable que es donde guardamos todos los datos de las bicicletas.
    bicicletas = cargar_los_elementos()

    conexion = conectar_bbdd()

    cursor = conexion.cursor()
    #Variable para introducir los datos en el MariaDB
    insert_script = "INSERT INTO bicicletas (url_imagen, marca, precio_inicial, precio_final, descuento) values(%s, %s, %s, %s, %s)"
    #Variable para resetear el id.
    reset_id = "ALTER TABLE bicicletas AUTO_INCREMENT = 1"

    cursor.execute(reset_id)

    # Bucle para meter todos los datos en la base de datos.
    for bicicleta in bicicletas:
        values = [bicicleta["url_imagen"], bicicleta["marca"], bicicleta["precio_inicial"], bicicleta["precio_final"], bicicleta["descuento"]]
        cursor.execute(insert_script, values)

    print("Carga de bicicletas finalizada")

    #Método para borrar los datos que hemos introducido en MariaDB.
def borrar_datos_tabla_bicicletas():
        conexion = conectar_bbdd()

        cursor = conexion.cursor()

        delete_script = "delete from bicicletas where id is not null"

        cursor.execute(delete_script)

        print("Borrado de bicicletas finaliza")

borrar_datos_tabla_bicicletas()

insertar_bicicletas()


