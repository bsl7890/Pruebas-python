# Aplicar correctamente los conceptos de modelamiento relacional, normalización y lenguaje SQL para desarrollar la estructura de una base de datos a partir de un escenario contextualizado, generando su correspondiente script SQL y representación gráfica inversa (reversa) mediante MySQL Workbench.

# 📝 Instrucción general para la actividad:

# En parejas, seleccionen (o trabajen con el escenario asignado) y desarrollen el modelo de base de datos relacional correspondiente. A partir del análisis, deberán:
# Crear el script SQL completo con todas las tablas normalizadas hasta la Tercera Forma Normal (3FN).
# Asegurarse de incluir todas las restricciones aprendidas en clases: PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, y tipos de datos adecuados.
# Realizar la reversa en MySQL Workbench para obtener el diagrama entidad-relación (ERD).
# Subir el script .sql a un repositorio de GitHub (uno por pareja).

# 📌 Entrega obligatoria:

#  Enviar el link del repositorio de GitHub con el script SQL y una imagen o archivo del modelo generado por reversa.


# 📘 Escenario 6: Gestión de Mantenimiento Vehicular
# La empresa de transporte TransRuta gestiona su flota mediante 
# un sistema de mantenimiento preventivo y correctivo. Cada acción queda 
# registrada con detalles de lo realizado y piezas usadas.
# Roles del sistema:
# Jefe de flota: programa mantenimientos y supervisa vehículos.
# Mecánico: ejecuta tareas y registra piezas.
# Administrador: gestiona personal y repuestos.
# Requerimientos:
# Vehículos: patente, tipo, año, estado, kilometraje.
# Mantenimientos: tipo (preventivo/correctivo), fecha, vehículo, técnico responsable.
# Mecánicos: nombre, RUT, especialidad.
# Repuestos: código, nombre, proveedor, costo.
# Uso de repuestos: mantenimiento, repuesto, cantidad.

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
    cursor.execute("CREATE DATABASE IF NOT EXISTS GESTION_MANTENIMIENTO")

    # Cambiar a la base de datos
    cursor.execute("USE GESTION_MANTENIMIENTO")

    print("Conexión y selección de base de datos exitosa.")
    # Crear tabla tipo_usuarios si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipo_usuarios (
            id_tipo INT AUTO_INCREMENT PRIMARY KEY,
            nombre_tipo VARCHAR(50) NOT NULL CHECK (nombre_tipo IN ('Jefe de Flota', 'Mecánico', 'Administrador')),
            descripcion_tipo VARCHAR(300) NOT NULL,
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
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL CHECK (CHAR_LENGTH(nombre) >= 3 AND nombre REGEXP '^[A-Za-z ]+$'),
            email VARCHAR(100) NOT NULL UNIQUE,
            fecha_registro DATE DEFAULT (CURRENT_DATE) NOT NULL,
            password VARCHAR(255) NOT NULL,
            activo BOOLEAN DEFAULT TRUE,
            edad TINYINT CHECK (edad BETWEEN 18 AND 100),
            id_tipo INT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (id_tipo) REFERENCES tipo_usuarios(id_tipo)
        )
    """)
    print("Tabla usuario creada o ya existe.")

    # Crear tabla vehiculos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
            patente VARCHAR(10) NOT NULL UNIQUE,
            year YEAR NOT NULL,
            kilometraje INT NOT NULL CHECK (kilometraje >= 0),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla vehiculos creada o ya existe.")

    # Crear tabla mantenimientos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mantenimientos (
            id_mantenimiento INT AUTO_INCREMENT PRIMARY KEY,
            fecha_mantenimiento DATE NOT NULL ,
            id_vehiculo INT NOT NULL CHECK (id_vehiculo > 0),
            id_usuario INT NOT NULL CHECK (id_usuario > 0),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo),
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
        )
    """)
    print("Tabla mantenimientos creada o ya existe.")
    # Crear tabla mecanicos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mecanicos (
            id_mecanico INT AUTO_INCREMENT PRIMARY KEY,
            id_usuario INT NOT NULL CHECK (id_usuario > 0),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)            
       )
    """)
    print("Tabla mecanicos creada o ya existe.")
    # Crear tabla repuestos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repuestos (
            id_repuesto INT AUTO_INCREMENT PRIMARY KEY,
            codigo VARCHAR(20) NOT NULL UNIQUE,
            nombre VARCHAR(100) NOT NULL,
            costo DECIMAL(10, 2) NOT NULL,
            stock INT NOT NULL CHECK (stock >= 0),
            descripcion VARCHAR(300),
            fecha_vencimiento DATE,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla repuestos creada o ya existe.")

    # Crear tabla tipo_repuestos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipo_repuestos (
            id_tipo_repuesto INT AUTO_INCREMENT PRIMARY KEY,
            nombre_tipo_repuesto VARCHAR(50) NOT NULL CHECK (nombre_tipo_repuesto IN ('Frenos', 'Aceite', 'Filtros', 'Baterías', 'Neumáticos')),
            descripcion VARCHAR(300) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla tipo_repuestos creada o ya existe.")

    # Alter table  tipo_repuestos
    cursor.execute("""ALTER TABLE repuestos
                        ADD COLUMN id_tipo_repuesto INT NOT NULL,
                        ADD FOREIGN KEY (id_tipo_repuesto) REFERENCES tipo_repuestos(id_tipo_repuesto)
                            """)
    print("Columna id_tipo_repuesto añadida a la tabla repuestos.")
    # Alter table mantenimientos
    cursor.execute("""ALTER TABLE mantenimientos
                        ADD COLUMN id_repuesto INT NOT NULL,
                        ADD FOREIGN KEY (id_repuesto) REFERENCES repuestos(id_repuesto)
                            """)
    print("Columna id_repuesto añadida a la tabla mantenimientos.")
    # Alter table mantenimientos
    cursor.execute("""ALTER TABLE mantenimientos
                        ADD COLUMN id_mecanico INT NOT NULL,
                        ADD FOREIGN KEY (id_mecanico) REFERENCES mecanicos(id_mecanico)
                   """)
    print("Columna id_mecanico añadida a la tabla mantenimientos.")
    print("Todas las tablas y relaciones creadas exitosamente.")

    # Crear personas si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            rut VARCHAR(12) PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL CHECK (CHAR_LENGTH(nombre) >= 3),
            fecha_nacimiento DATE NOT NULL,
            telefono VARCHAR(15),
            direccion VARCHAR(255),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla personas creada o ya existe.")
    # Alter table usuario para añadir rut
    cursor.execute("""
        ALTER TABLE usuarios
        ADD COLUMN rut VARCHAR(12) NOT NULL UNIQUE,
        ADD FOREIGN KEY (rut) REFERENCES personas(rut)
    """)
    # Crear estado_vehiculo si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estado_vehiculo (
            id_estado INT AUTO_INCREMENT PRIMARY KEY,
            estado VARCHAR(20) NOT NULL CHECK (estado IN ('Activo', 'Inactivo', 'En Mantenimiento')),
            descripcion VARCHAR(50) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)

    # Alter table vehiculos para añadir estado
    cursor.execute("""
        ALTER TABLE vehiculos
        ADD COLUMN id_estado INT NOT NULL,
        ADD FOREIGN KEY (id_estado) REFERENCES estado_vehiculo(id_estado)
    """)
    print("Columna id_estado añadida a la tabla vehiculos.")

    # Crear tipo_vehiculo si no existe
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS tipo_vehiculo (
            id_tipo_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
            tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('Camión', 'Bus', 'Furgoneta', 'Auto')),
            descripcion VARCHAR(300) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
        """)
    print("Tabla tipo_vehiculo creada o ya existe.")
    # Alter table vehiculos para añadir tipo_vehiculo
    cursor.execute("""
            ALTER TABLE vehiculos
            ADD COLUMN id_tipo_vehiculo INT NOT NULL,
            ADD FOREIGN KEY (id_tipo_vehiculo) REFERENCES tipo_vehiculo(id_tipo_vehiculo)
        """)
    print("Columna id_tipo_vehiculo añadida a la tabla vehiculos.")

    # Crear tabla especialidad_mecanico si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS especialidad_mecanico (
            id_especialidad INT AUTO_INCREMENT PRIMARY KEY,
            especialidad VARCHAR(50) NOT NULL  CHECK (especialidad IN ('Mecánica General', 'Electricidad Automotriz', 'Transmisiones', 'Suspensión y Dirección')),
            descripcion VARCHAR(300) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla especialidad_mecanico creada o ya existe.")
    # Alter table mecanicos para añadir especialidad
    cursor.execute("""
            ALTER TABLE mecanicos
            ADD COLUMN id_especialidad INT NOT NULL,
            ADD FOREIGN KEY (id_especialidad) REFERENCES especialidad_mecanico(id_especialidad)
    """)
    print("Columna id_especialidad añadida a la tabla mecanicos.")

    # Crear tabla tipo_mantenimiento si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipo_mantenimiento (
            id_tipo_mantenimiento INT AUTO_INCREMENT PRIMARY KEY,
            tipo_mantenimiento VARCHAR(20) NOT NULL CHECK (tipo_mantenimiento IN ('Preventivo', 'Correctivo')),
            descripcion VARCHAR(300) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla tipo_mantenimiento creada o ya existe.")
    # Alter table mantenimientos para añadir tipo_mantenimiento
    cursor.execute("""
            ALTER TABLE mantenimientos
            ADD COLUMN id_tipo_mantenimiento INT NOT NULL,
            ADD FOREIGN KEY (id_tipo_mantenimiento) REFERENCES tipo_mantenimiento(id_tipo_mantenimiento)
    """)
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()


