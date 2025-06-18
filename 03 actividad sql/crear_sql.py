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
        CREATE TABLE IF NOT EXISTS usuario (
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
            tipo VARCHAR(50) NOT NULL,
            anio YEAR NOT NULL,
            estado VARCHAR(20) NOT NULL CHECK (estado IN ('Activo', 'Inactivo', 'En Mantenimiento')),
            kilometraje INT NOT NULL,
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
            tipo_mantenimiento VARCHAR(20) NOT NULL CHECK (tipo_mantenimiento IN ('Preventivo', 'Correctivo')),
            fecha DATE NOT NULL,
            id_vehiculo INT NOT NULL,
            tecnico_responsable VARCHAR(100) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
        )
    """)
    print("Tabla mantenimientos creada o ya existe.")
    # Crear tabla mecanicos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mecanicos (
            id_mecanico INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            rut VARCHAR(12) NOT NULL UNIQUE,
            especialidad VARCHAR(50) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla mecanicos creada o ya existe.")

    # Crear tabla repuestos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repuestos (
            id_repuesto INT AUTO_INCREMENT PRIMARY KEY,
            codigo VARCHAR(20) NOT NULL UNIQUE,
            nombre VARCHAR(100) NOT NULL,
            proveedor VARCHAR(100) NOT NULL,
            costo DECIMAL(10, 2) NOT NULL,
            stock INT NOT NULL CHECK (stock >= 0),
            descripcion VARCHAR(300),
            tipo_repuesto VARCHAR(50) NOT NULL CHECK (tipo_repuesto IN ('Frenos', 'Aceite', 'Filtros', 'Baterías', 'Neumáticos')),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_by INT,
            updated_by INT,
            deleted BOOLEAN DEFAULT FALSE
        )
    """)
    print("Tabla repuestos creada o ya existe.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()


