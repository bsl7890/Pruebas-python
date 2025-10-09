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
    cursor.execute("CREATE DATABASE IF NOT EXISTS ejemploSelect")

    # Cambiar a la base de datos
    cursor.execute("USE ejemploSelect")

    # Tabla: tipo_usuarios
    cursor.execute("""--sql CREATE TABLE IF NOT EXISTS tipo_usuarios (
                id_tipo INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                nombre_tipo VARCHAR(50) NOT NULL CHECK (nombre_tipo in ('Administrador','Cliente','Moderador')), 
                descripcion_tipo VARCHAR(200) NOT NULL
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_by INT,
                updated_by INT,
                deleted BOOLEAN DEFAULT FALSE
                );""")
    # deleted sirve para borrado lógico de registros (no se elimina físicamente)
    

    # Tabla: usuarios (se añade campo created_at con valor por defecto)
    cursor.execute("""--sql CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(200) NOT NULL CHECK,
                email VARCHAR(100) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id_tipo_usuario INT,
                CONSTRAINT fk_usuarios_tipo_usuarios FOREIGN KEY (id_tipo_usuario) REFERENCES tipo_usuarios(id_tipo)
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_by INT,
                updated_by INT,
                deleted BOOLEAN DEFAULT FALSE
                );""")

    # Tabla: ciudad (nueva)
    cursor.execute("""--sql CREATE TABLE IF NOT EXISTS ciudad (
                id_ciudad INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                nombre_ciudad VARCHAR(100) NOT NULL CHECK,
                region VARCHAR(100)
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_by INT,
                updated_by INT,
                deleted BOOLEAN DEFAULT FALSE
                );""")

    # Tabla: personas (relacionada con usuarios y ciudad)
    cursor.execute("""--sql CREATE TABLE personas (
                rut VARCHAR(12) PRIMARY KEY NOT NULL,
                nombre_completo VARCHAR(100) NOT NULL CHECK ,
                fecha_nac DATE,
                id_usuario INT,
                id_ciudad INT,
                CONSTRAINT fk_personas_usuarios FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                CONSTRAINT fk_personas_ciudad FOREIGN KEY (id_ciudad) REFERENCES ciudad(id_ciudad)
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_by INT,
                updated_by INT,
                deleted BOOLEAN DEFAULT FALSE
                );""")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
