import mysql.connector

try:
    # Conexión inicial
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        port=3306
    )
    cursor = conn.cursor()

    # Crear la base de datos si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS tienda_demo")
    print("Base de datos 'tienda_demo' creada.")
    # Cambiar a la base de datos
    #DELIMITER
    cursor.execute("USE tienda_demo")
    print("Base de datos 'tienda_demo' seleccionada.")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
    print("Conexión cerrada.")