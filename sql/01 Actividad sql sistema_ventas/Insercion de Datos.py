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

    # Verificar si el usuario técnico ya existe (por correo)
    cursor.execute("SELECT id FROM usuarios WHERE correo = 'admintech@example.com'")
    resultado = cursor.fetchone()

    # Insertar usuario técnico inicial (sin tipo) para auditoría
    # Si el usuario existe, usar su ID; si no, crear el usuario y obtener su ID
    if resultado:
        usuario_tecnico_id = resultado[0] 
        print("Usuario técnico ya existe con ID:", usuario_tecnico_id)
    else:
        sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('admintech', 'admintech@example.com', 'admin123', NULL, NULL, NULL)"
        cursor.execute(sql)
        conn.commit()
        usuario_tecnico_id = cursor.lastrowid # ID del nuevo usuario técnico creado
        print("Usuario técnico creado con ID:", usuario_tecnico_id)

    # 3. Insertar tipos de usuario
    sql_admin = "INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by) VALUES ('Administrador', 'Usuario con acceso total al sistema', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql_admin)
    sql_vendedor = "INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by) VALUES ('Vendedor', 'Usuario encargado de realizar ventas', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql_vendedor)
    sql_cajero = "INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by) VALUES ('Cajero', 'Usuario que realiza cobros y pagos', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql_cajero)
    sql_cliente = "INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by) VALUES ('Cliente', 'Usuario que compra productos', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql_cliente)
    sql_invitado = "INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by) VALUES ('Invitado', 'Usuario con acceso limitado', " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql_invitado)
    conn.commit()
    print("Tipos de usuario creados")

    # Obtener IDs de tipos
    cursor.execute("SELECT id FROM tipo_usuarios WHERE nombre_tipo='Administrador'")# Insertar tipo de usuario Administrador
    tipo_admin_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM tipo_usuarios WHERE nombre_tipo='Vendedor'") # Insertar tipo de usuario Vendedor
    tipo_vendedor_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM tipo_usuarios WHERE nombre_tipo='Cajero'")# Insertar tipo de usuario Administrador
    tipo_cajero_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM tipo_usuarios WHERE nombre_tipo='Cliente'") # Insertar tipo de usuario Vendedor
    tipo_cliente_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM tipo_usuarios WHERE nombre_tipo='Invitado'") # Insertar tipo de usuario Vendedor
    tipo_invitado_id = cursor.fetchone()[0]
    

    # 4. Insertar usuarios asociados a tipos
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('adminuser', 'admin@example.com', 'admin123', " + str(tipo_admin_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('vendedor1', 'vendedor1@example.com', 'venta123', " + str(tipo_vendedor_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('cajero1', 'cajero@example.com', 'cajero123', " + str(tipo_cajero_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('cliente1', 'cliente@example.com', 'cliente123', " + str(tipo_cliente_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('invitado2', 'invitado@example.com', 'invitado123', " + str(tipo_invitado_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('vendedor2', 'vendedor2@example.com', 'venta123', " + str(tipo_vendedor_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('vendedor3', 'vendedor3@example.com', 'venta123', " + str(tipo_vendedor_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('vendedor4', 'vendedor4@example.com', 'venta123', " + str(tipo_vendedor_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO usuarios (nombre_usuario, correo, password, tipo_usuario_id, created_by, updated_by) VALUES ('vendedor5', 'vendedor5@example.com', 'venta123', " + str(tipo_vendedor_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    
    conn.commit()
    print("Usuarios creados")

    # 5. Insertar productos
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by) VALUES ('Laptop Dell', 'Laptop i5 con 8GB RAM', 650000, 10, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by) VALUES ('Mouse Logitech', 'Mouse inalámbrico', 15000, 50, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by) VALUES ('Teclado Mecánico', 'Teclado con luces RGB', 30000, 30, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by) VALUES ('Monitor Samsung', 'Monitor 24 pulgadas Full HD', 120000, 15, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO productos (nombre_producto, descripcion_producto, precio, stock, created_by, updated_by) VALUES ('Audífonos Sony', 'Audífonos Bluetooth', 45000, 40, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    conn.commit()
    print("Productos creados")

    # Obtener IDs usuarios para ventas
    cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario='vendedor1'")  
    vendedor1_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario='vendedor2'")
    vendedor2_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario='vendedor3'")
    vendedor3_id = cursor.fetchone()[0]    
    cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario='vendedor4'")
    vendedor4_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM usuarios WHERE nombre_usuario='vendedor5'")
    vendedor5_id = cursor.fetchone()[0]
    
    # 6. Insertar ventas
    sql = "INSERT INTO ventas (usuario_id, created_by, updated_by) VALUES (" + str(vendedor1_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO ventas (usuario_id, created_by, updated_by) VALUES (" + str(vendedor2_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO ventas (usuario_id, created_by, updated_by) VALUES (" + str(vendedor3_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO ventas (usuario_id, created_by, updated_by) VALUES (" + str(vendedor4_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO ventas (usuario_id, created_by, updated_by) VALUES (" + str(vendedor5_id) + ", " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    conn.commit()
    print("Ventas creadas")

    #Obtener IDs ventas y productos
    cursor.execute("SELECT id FROM ventas ORDER BY id ASC")
    ventas = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM productos ORDER BY id ASC")
    productos = [row[0] for row in cursor.fetchall()]

    # 7. Insertar detalle_venta
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by) VALUES (" + str(ventas[0]) + ", " + str(productos[0]) + ", 1, 650000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by) VALUES (" + str(ventas[0]) + ", " + str(productos[1]) + ", 2, 15000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by) VALUES (" + str(ventas[1]) + ", " + str(productos[1]) + ", 1, 15000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by) VALUES (" + str(ventas[1]) + ", " + str(productos[2]) + ", 1, 30000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    sql = "INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario, created_by, updated_by) VALUES (" + str(ventas[1]) + ", " + str(productos[2]) + ", 1, 30000, " + str(usuario_tecnico_id) + ", " + str(usuario_tecnico_id) + ")"
    cursor.execute(sql)
    conn.commit()
    print("Detalles de ventas creados")

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conn.close()
