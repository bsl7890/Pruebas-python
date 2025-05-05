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
    cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_ventas")

    # Cambiar a la base de datos
    cursor.execute("USE sistema_ventas")

    print("Conexión y selección de base de datos exitosa.")

    # Crear tabla tipo_usuarios si no existe
    #id identificador único
    #nombre Tipo de usuario (Admin, Cliente)
    # Campos de audotoria
    #created_at Fecha creacion
    #updated_at Fecha de modificacion
    #created_by Usuario que crea
    #updated_by Usuario que modifica
    #deleted Borrador logico
    cursor.execute("""CREATE TABLE IF NOT EXISTS tipo_usuarios (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre_tipo VARCHAR(50) NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        created_by INT, 
                        updated_by INT,
                        deleted BOOLEAN DEFAULT FALSE)""")
    conn.commit() 

    cursor.execute('''ALTER TABLE tipo_usuarios
                        ADD descripcion_tipo VARCHAR(200) NOT NULL AFTER nombre_tipo;
                        ''')
    
    print("Tabla tipo_usuarios creada exitosamente.")
    # Crear tabla usuarios si no existe
    #id identificador único
    #nombre_tipo Nombre de usuario
    #correo Correo electrónico único
    #tipo_usuario_id Relación a tipo_usuario
    # Campos de audotoria
    #created_at Fecha creacion
    #updated_at Fecha de modificacion
    #created_by Usuario que crea
    #updated_by Usuario que modifica
    #deleted Borrador logico
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre_tipo VARCHAR(100) NOT NULL,
                        correo VARCHAR(100) UNIQUE,
                        tipo_usuario_id INT,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        created_by INT, 
                        updated_by INT,
                        deleted BOOLEAN DEFAULT FALSE)""")
    # Si la clave foránea ya existe, la eliminamos antes de crearla de nuevo
    cursor.execute('''ALTER TABLE usuarios
                    DROP FOREIGN KEY fk_usuario_tipo_usuario''')
    
    cursor.execute('''ALTER TABLE usuarios
                        CHANGE COLUMN nombre_tipo nombre_usuario VARCHAR(100) NOT NULL;
                        ''')
    cursor.execute('''ALTER TABLE usuarios
                        ADD password VARCHAR(45) NOT NULL AFTER nombre_usuario;
                        ''')

    # Agregar la clave foránea correctamente
    cursor.execute('''ALTER TABLE usuarios
                    ADD CONSTRAINT fk_usuario_tipo_usuario
                    FOREIGN KEY (tipo_usuario_id) REFERENCES
                    tipo_usuarios(id);''')

    conn.commit()
    print("Tabla usuarios creada exitosamente.")

    # Crear tabla productos si no existe
    #id identificador único
    #nombre_pruducto Nombre del producto
    #precio El precio del producto
    #stock La cantidad disponible de cada producto.
    # Campos de audotoria
    #created_at Fecha creacion
    #updated_at Fecha de modificacion
    #created_by Usuario que crea
    #updated_by Usuario que modifica
    #deleted Borrador logico
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre_producto VARCHAR(100) NOT NULL,
                    precio FLOAT NOT NULL,
                    stock INT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    created_by INT, 
                    updated_by INT,
                    deleted BOOLEAN DEFAULT FALSE)""")
    conn.commit() 
    print("Tabla productos creada exitosamente.")

    # Crear tabla productos si no existe
    #id identificador único
    #usuario_id ID del usuario que realiza la venta
    #fecha_venta Fecha y hora de la venta
    # Campos de audotoria
    #created_at Fecha creacion
    #updated_at Fecha de modificacion
    #created_by Usuario que crea
    #updated_by Usuario que modifica
    #deleted Borrador logico
    cursor.execute("""CREATE TABLE IF NOT EXISTS ventas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        usuario_id INT,
                        fecha_venta DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        created_by INT, 
                        updated_by INT,
                        deleted BOOLEAN DEFAULT FALSE)""")

    # Eliminar clave foránea si existe
    cursor.execute('''ALTER TABLE ventas DROP FOREIGN KEY fk_usuario_ventas''')

    cursor.execute('''ALTER TABLE ventas
                        ADD CONSTRAINT fk_usuario_ventas
                        FOREIGN KEY (usuario_id) REFERENCES
                        usuarios(id);''')
    conn.commit() 
    print("Tabla ventas creada exitosamente.")

    # Crear tabla detalle_ventas si no existe
    #id identificador único
    #venta_id ID de la venta a la que pertenece el detalle
    #producto:id ID del producto que se vendió
    #cantidad Cantidad del producto vendido
    #precio_unitario Precio unitario del producto en la venta
    # Campos de audotoria
    #created_at Fecha creacion
    #updated_at Fecha de modificacion
    #created_by Usuario que crea
    #updated_by Usuario que modifica
    #deleted Borrador logico
    cursor.execute("""CREATE TABLE IF NOT EXISTS detalle_ventas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        venta_id INT,
                        producto_id INT,
                        cantidad INT NOT NULL,
                        precio_unitario FLOAT DEFAULT 0 NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                        created_by INT, 
                        updated_by INT,
                        deleted BOOLEAN DEFAULT FALSE)""")
    cursor.execute('''ALTER TABLE detalle_ventas DROP FOREIGN KEY fk_ventas_detalle_ventas''')
    cursor.execute('''ALTER TABLE detalle_ventas DROP FOREIGN KEY fk_productos_detalle_ventas''')

    cursor.execute('''ALTER TABLE detalle_ventas
                        ADD CONSTRAINT fk_ventas_detalle_ventas
                        FOREIGN KEY (venta_id) REFERENCES
                        ventas(id);''')
    cursor.execute('''ALTER TABLE detalle_ventas
                        ADD CONSTRAINT fk_productos_detalle_ventas
                        FOREIGN KEY (producto_id) REFERENCES
                        productos(id);''')
    conn.commit() 
    print("Tabla detalle_ventas creada exitosamente.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
