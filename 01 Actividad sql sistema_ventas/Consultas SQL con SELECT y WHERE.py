import mysql.connector # Importar mysql.connector para manejar la conexión a la base de datos
from datetime import datetime # Importar datetime para manejar fechas y horas

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="sistema_ventas",
        port=3306
    )
    cursor = conn.cursor()
    print("Conexión a la base de datos exitosa.")


 # a. Personas activas
    print("\n[a]Nombre de personas activas: ")
    cursor.execute("SELECT nombre_usuario FROM usuarios WHERE deleted = 1")
    for fila in cursor.fetchall():
        print("Usuario activo:", fila[0])


    # b. Usuarios con tipo 'Administrador'  
    print("\n[b]Usuario con tipo 'Administrador':")
    cursor.execute("""
        SELECT nombre_usuario FROM usuarios
        WHERE tipo_usuario_id = 1
    """)
    for fila in cursor.fetchall():
        print("Usuario tipo Administrador:", fila[0])

    

    # c. Usuarios que comienzan con 'a'
    print("\n[c] Usuarios que comienzan con 'a':")
    cursor.execute("SELECT nombre_usuario FROM usuarios WHERE nombre_usuario LIKE 'a%'")
    for fila in cursor.fetchall():
        print(fila)

    # d. Personas creadas entre dos fechas
    print("\n[d] Personas creadas entre 2025-01-01 y 2025-12-31:")
    cursor.execute("""
        SELECT nombre_usuario, correo, created_at
        FROM usuarios
        WHERE created_at BETWEEN '2025-01-01' AND '2025-12-31'
        """)
    for fila in cursor.fetchall():
        print(fila)

    # 1. Mostrar a los usuarios vendedores
    print("\n[1] Usuarios con tipo vendedor: ")
    cursor.execute("""
        SELECT nombre_usuario FROM usuarios
        WHERE tipo_usuario_id = 2
        """)
    for fila in cursor.fetchall():
        print(fila)

    # 2. Usuarios cambiar a los vendedores a activo
    print("\n[2] Cambiar vendedores a activo:")
    cursor.execute("""
        UPDATE usuarios
        SET deleted = 1
        WHERE tipo_usuario_id = 2
        """)
    conn.commit()  # Confirmar los cambios en la base de datos
    print("Se actualizaron los vendedores a estado activo.")

    # 3. Usuarios cuyo correo contiene 'example'
    print("\n[3] Correos con 'example':")
    cursor.execute("SELECT nombre_usuario, correo FROM usuarios WHERE correo LIKE '%example%'")
    for fila in cursor.fetchall():
        print(fila)

    # 4. Productos con stock bajo (menor a 20)
    print("\n[4] Productos con con stock bajo menor a 20:")
    cursor.execute("SELECT nombre_producto, stock FROM productos WHERE stock < 20")
    for fila in cursor.fetchall():
        print(fila)

    # 5. Personas activas creadas después del 2025-01-01
    print("\n[5] Personas activas creadas después de 2025-01-01:")
    cursor.execute("""
        SELECT nombre_usuario, correo, created_at
        FROM usuarios
        WHERE deleted = 1 AND created_at > '2025-01-01'
        """)
    for fila in cursor.fetchall():
        print(fila)

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conn.close()