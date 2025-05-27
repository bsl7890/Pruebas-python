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
    # Obtener fecha y hora actual en formato compatible con MySQL
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verificar si el usuario técnico ya existe (por correo)
    cursor.execute("SELECT id FROM usuarios WHERE correo = 'admintech@example.com'")
    resultado = cursor.fetchone()

    # Insertar usuario técnico inicial (sin tipo) para auditoría
    # Si el usuario existe, usar su ID; si no, crear el usuario y obtener su ID
    if resultado:
        usuario_tecnico_id = resultado[0] # ID del usuario técnico existente
        print("Usuario técnico ya existe con ID:", usuario_tecnico_id)
    else:
        sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by, created_at, updated_at, deleted) VALUES ('admintech', 'admintech@example.com', 'admin123', NULL, NULL, NULL, '" + now + "', '" + now + "', 0)"
        cursor.execute(sql)
        conn.commit()
        usuario_tecnico_id = cursor.lastrowid # ID del nuevo usuario técnico creado
        print("Usuario técnico creado con ID:", usuario_tecnico_id)

    # 2. Insertar tipos de usuario

    sql_admin = "INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by, created_at, updated_at, deleted) VALUES ('Administrador', 'Usuario con acceso total al sistema', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql_admin)
    sql_vendedor = "INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by, created_at, updated_at, deleted) VALUES ('Vendedor', 'Usuario encargado de realizar ventas', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql_vendedor)
    conn.commit()
    print("Tipos de usuario creados")

    # 3. Obtener IDs de tipos
    cursor.execute("SELECT id FROM tipo_usuarios WHERE nombre_tipo='Administrador'")# Insertar tipo de usuario Administrador
    tipo_admin_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM tipo_usuarios WHERE nombre_tipo='Vendedor'") # Insertar tipo de usuario Vendedor
    tipo_vendedor_id = cursor.fetchone()[0]

    # 4. Insertar usuarios asociados a tipos
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by, created_at, updated_at, deleted) VALUES ('adminuser', 'admin@example.com', 'admin123', " + str(tipo_admin_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by, created_at, updated_at, deleted) VALUES ('vendedor1', 'ventas1@example.com', 'venta123', " + str(tipo_vendedor_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by, created_at, updated_at, deleted) VALUES ('vendedor2', 'ventas2@example.com', 'venta123', " + str(tipo_vendedor_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    conn.commit()
    print("Usuarios creados")

    # 5. Insertar productos
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by, created_at, updated_at, deleted) VALUES ('Laptop Dell', 'Laptop i5 con 8GB RAM', 650000, 10, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by, created_at, updated_at, deleted) VALUES ('Mouse Logitech', 'Mouse inalámbrico', 15000, 50, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by, created_at, updated_at, deleted) VALUES ('Teclado Mecánico', 'Teclado con luces RGB', 30000, 30, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    conn.commit()
    print("Productos creados")

    # 6. Obtener IDs usuarios para ventas
    cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario='vendedor1'")
    vendedor1_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario='vendedor2'")
    vendedor2_id = cursor.fetchone()[0]

    # 7. Insertar ventas
    sql = "INSERT INTO ventas (usuario_id, fecha_venta, created_by, updated_by, created_at, updated_at, deleted) VALUES (" + str(vendedor1_id) + ", '" + now + "', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO ventas (usuario_id, fecha_venta, created_by, updated_by, created_at, updated_at, deleted) VALUES (" + str(vendedor2_id) + ", '" + now + "', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    conn.commit()
    print("Ventas creadas")

    # 8. Obtener IDs ventas y productos
    cursor.execute("SELECT id FROM ventas ORDER BY id ASC")
    ventas = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM productos ORDER BY id ASC")
    productos = [row[0] for row in cursor.fetchall()]

    # 9. Insertar detalle_venta
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by, created_at, updated_at, deleted) VALUES (" + str(ventas[0]) + ", " + str(productos[0]) + ", 1, 650000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by, created_at, updated_at, deleted) VALUES (" + str(ventas[0]) + ", " + str(productos[1]) + ", 2, 15000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by, created_at, updated_at, deleted) VALUES (" + str(ventas[1]) + ", " + str(productos[1]) + ", 1, 15000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by, created_at, updated_at, deleted) VALUES (" + str(ventas[1]) + ", " + str(productos[2]) + ", 1, 30000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ", '" + now + "', '" + now + "', 0)"
    cursor.execute(sql)
    conn.commit()
    print("Detalles de ventas creados")

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conn.close()
