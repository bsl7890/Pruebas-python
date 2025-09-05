import mysql.connector

try:
    # Conexión inicial
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="ejemploSelect",
        port=3306
    )
    cursor = conn.cursor()

    print("Conexión a la base de datos exitosa.")

    # -- 1.-  Mostrar todos los usuarios de tipo Cliente
    # -- Seleccionar nombre de usuario, correo y tipo_usuario

    cursor.execute("""--sql """)

    # -- 2.-  Mostrar Personas nacidas despues del año 1990
    # -- Seleccionar Nombre, fecha de nacimiento y username.

    cursor.execute("""--sql """)

    # -- 3.- Seleccionar nombres de personas que comiencen con la 
    # -- letra A - Seleccionar nombre y correo la persona.

    cursor.execute("""--sql """)

    # -- 4.- Mostrar usuarios cuyos dominios de correo sean
    # -- mail.commit LIKE '%mail.com%'

    cursor.execute("""--sql """)

    # -- 5.- Mostrar todas las personas que no viven en 
    # -- Valparaiso y su usuario + ciudad.
    # -- select * from ciudad; -- ID 2 VALPARAISO

    cursor.execute("""--sql """)

    # -- 6.- Mostrar usuarios que contengan más de 7 
    # -- carácteres de longitud.

    cursor.execute("""--sql """)

    # -- 7.- Mostrar username de personas nacidas entre
    # -- 1990 y 1995

    cursor.execute("""--sql """)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()