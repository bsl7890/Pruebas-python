import mysql.connector

try:
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host="127.0.0.1",   # Dirección de la base de datos (localhost)
        user="root",         # Usuario de MySQL
        password="1234",     # Contraseña de MySQL
        database="inventario_tienda",  # Nombre de la base de datos
        port=3306            # Puerto de conexión (3306 por defecto para MySQL)
    )

    cursor = conn.cursor()

    # Crear la tabla productos si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,  # ID único, auto incrementado
        nombre VARCHAR(100) NOT NULL,       # Nombre del producto
        descripcion TEXT,                   # Descripción del producto
        precio DECIMAL(10, 2),              # Precio del producto (hasta 10 dígitos, 2 decimales)
        stock INT                           # Cantidad en inventario
    );
    """)

    print("Tabla 'productos' creada con éxito ✅")

    # --- Paso 1: Insertar un producto ---
    sql = "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
    valores = ("Monitor Gamer", "Monitor de 24 pulgadas 144Hz", 199.99, 10)

    cursor.execute(sql, valores)
    conn.commit()

    print("✅ Producto insertado con éxito")

    # --- Paso 2: Actualizar el stock de un producto ---
    # Imaginemos que queremos cambiar el stock del producto con id = 1
    sql_update = "UPDATE productos SET stock = %s WHERE id = %s"
    nuevos_valores = (15, 1)  # Actualizamos el stock a 15 para el producto con id=1

    cursor.execute(sql_update, nuevos_valores)
    conn.commit()

    print("✅ Stock del producto actualizado con éxito")

    # --- Paso 3: Eliminar un producto ---
    # Imaginemos que queremos eliminar el producto con id = 1
    sql_delete = "DELETE FROM productos WHERE id = %s"
    id_a_eliminar = (1,)  # El producto con id = 1 será eliminado

    cursor.execute(sql_delete, id_a_eliminar)
    conn.commit()

    print("✅ Producto eliminado con éxito")

    # --- Paso 4: Consultar todos los productos ---
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()

    print("📦 Productos en la base de datos:")
    for fila in resultados:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Descripción: {fila[2]}, Precio: ${fila[3]}, Stock: {fila[4]} unidades")

except mysql.connector.Error as err:
    print("Error al interactuar con la base de datos:", err)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión a la base de datos cerrada. 👋")