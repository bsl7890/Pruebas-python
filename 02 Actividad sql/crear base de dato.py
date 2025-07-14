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
    cursor.execute("CREATE DATABASE IF NOT EXISTS EJEMPLO_CHECK")

    # Cambiar a la base de datos
    cursor.execute("USE EJEMPLO_CHECK")


    print("Conexión y selección de base de datos exitosa.")


    # Crear tabla tipo_usuarios si no existe
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tipo_usuarios (
            id_tipo INT AUTO_INCREMENT PRIMARY KEY,
            nombre_tipo VARCHAR(50) NOT NULL CHECK (nombre_tipo IN ('Estudiante', 'Profesor', 'Administrador')),
            descripcion_tipo VARCHAR(300) NOT NULL ,
            nivel_acceso TINYINT CHECK (nivel_acceso BETWEEN 1 AND 3),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT, 
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla tipo_usuarios creada o ya existe.")



    # Crear tabla usuario si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL CHECK (CHAR_LENGTH(nombre) >= 3 AND nombre REGEXP '^[A-Za-z ]+$'),
            email VARCHAR(100) NOT NULL UNIQUE,
            fecha_registro DATE DEFAULT (CURRENT_DATE) NOT NULL,
            password VARCHAR(255) NOT NULL,
            activo BOOLEAN DEFAULT TRUE,
            edad TINYINT CHECK (edad BETWEEN 13 AND 100),
            id_tipo INT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT, 
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla usuario creada o ya existe.")

    # Agregar clave foránea a la tabla usuario
    cursor.execute("""
        ALTER TABLE usuario
        ADD CONSTRAINT fk_tipo_usuario
        FOREIGN KEY (id_tipo) REFERENCES tipo_usuarios(id_tipo)
        """)    

    # Crear tabla curso si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS curso (
            id_curso INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(200) NOT NULL CHECK (CHAR_LENGTH(titulo) BETWEEN 5 AND 200),
            duracion_horas DECIMAL(4,2) CHECK (duracion_horas > 0 AND duracion_horas <= 100),
            nivel VARCHAR(20) CHECK (nivel IN ('Principiante', 'Intermedio', 'Avanzado')),
            precio DECIMAL(10,2) CHECK (precio >= 0),
            fecha_publicacion DATE CHECK (fecha_publicacion >= '2020-01-01'),
            CHECK (
                (nivel = 'Principiante' AND precio <= 50) OR
                (nivel IN ('Intermedio', 'Avanzado') AND precio <= 200)
            ),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT, 
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )""")
    print("Tabla curso creada o ya existe.")


    # Crear tabla inscripciones si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inscripciones (
            id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
            id_usuario INT NOT NULL,
            id_curso INT NOT NULL,
            fecha_inscripcion DATE DEFAULT (CURRENT_DATE) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT, 
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
        """)
    print("Tabla inscripciones creada o ya existe.")

    cursor.execute("""
        ALTER TABLE inscripciones
        ADD CONSTRAINT fk_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        """)
    cursor.execute("""
        ALTER TABLE inscripciones
        ADD CONSTRAINT fk_curso
        FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
        """)
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
