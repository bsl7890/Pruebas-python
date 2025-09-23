# ENCUENSTA DE LOS CLIENTES
# Nombre del Cliente: Cronodosis
# Fecha: 23/09/2025
# Nombre del Analista: Benjamin Santander


# Objetivos y Alcance
# ¿Cuál es el objetivo principal del sistema que necesita?
# R: que las personas puedan gestionar la toma de sus medicamentos

# ¿Qué problemas actuales busca resolver con esta solución?
# R: Buscan solucionar la mala gestión de consumo de alimentos

# ¿Qué procesos quiere mejorar o automatizar?
# 	R:quiere mejorar la toma de sus medicamentos optimizando la gestión de alarmas y medicamentos con una aplicación móvil o web .

# ¿Qué espera obtener como resultado final del sistema (reportes, gráficos,
# control de stock, etc.)?
# 	R: Sistema que se conecte a un pastillero mediante una sección de alarma e inicio de sesión confiable. Alarma que sea digital.
# 	   La aplicación móvil que tenga un panel de control donde uno será para revisar el perfil de la persona o cambio de contraseña o quiere eliminar cuenta y otra parte agendar medicamento que se conecte con las alarmas.

# historial donde se guardara los medicamento ingresado dia, hora y los medicamento que les falta por tomar y historial de medicamento sin tomar,

# Una sección del los medicamentos donde se muestre el historial

# 1 alarma por cada medicamento



	
# Usuarios y Roles
# ¿Quiénes serán los usuarios principales del sistema? (ejemplo:
# administrador, cliente, empleado)
# 	R: administrador, usuario, tutor(opcional)

# ¿Cada usuario tendrá los mismos permisos o se necesitan diferentes niveles
# de acceso?
# 	R: El administrador controla todo y el usuario tendrá permisos predeterminados como cambiar idioma, tema de la página y su perfil el tutor controlara lo que hacen los usuarios podran revisar sus historial sus alarma (monitoriar al usuario).

# ¿Cuántos usuarios utilizarán el sistema simultáneamente?
# 	R: Un usuario puede tener un pastillero solamente.

# ¿Qué información necesita guardar sobre cada entidad?
# (por ejemplo, si hablamos de clientes: nombre, RUT, dirección, teléfono,
# correo, fecha de registro)
# 	R: 
# usuario: nombre_usuario, correo, rut, contraseña, número de teléfono, edad, género, alergias, enfermedades crónicas, frecuencia de tratamiento, tipo de tratamiento, duración de tratamiento 

# administrador: nombre_administrador, correo, rut, contraseña
# tutor: nombre_tutor, correo, rut, contraseña, nombre_usuario, (todos los datos)

# ¿Qué datos son obligatorios y cuáles opcionales?
# 	R: Para el usuario común todos los datos son obligatorios, el administrador tiene como obligación el nombre, correo y contraseña al igual que el tutor. 

# ¿Existen datos que deban mantenerse históricos (por ejemplo: precios
# anteriores, estados de pedidos, cambios de dirección)?
# 	R: Todo el historial de  medicamentos.

# ¿Existen datos sensibles que deban protegerse (por ejemplo: datos
# personales, información financiera)?
# 	R: Todos los datos.


# Procesos y Relaciones:

# ¿Qué procesos principales debe registrar el sistema?
# (ejemplo: ventas, compras, préstamos, devoluciones, reservas)
# 	R: El historial del pastillero

# ¿Cómo se relacionan las entidades entre sí? (un cliente puede hacer muchos
# pedidos, un pedido tiene muchos productos, etc.)
# 	R: El usuario puede tener un pastillero, el usuario puede tener muchas alarmas.
# 	El tutor puede tener muchos usuarios, el usuario puede tener un tutor.
# Muchos medicamentos pueden tener muchas alarmas.
# ¿Qué reglas de negocio existen?
# (ejemplo: un libro puede ser prestado a un solo socio a la vez, el stock no
# puede ser negativo)
# 	R: El tutor sólo puede tener hasta 5 usuarios vinculados, si un usuario tiene un tutor se le restringen el acceso a editar sus alarma y medicamentos, un usuario “puede” tener un tutor

# Reportes y Consultas:
# ¿Qué reportes debe poder generar el sistema?
# (por ejemplo: ventas por mes, libros más prestados, clientes más activos)
# 	R: reporte mensual al tutor y al usuario(sin tutor)

# ¿Necesita filtros o búsquedas específicas?
# (por rango de fechas, por estado de pedido, por categoría, etc.)
# 	R: Rango de fechas, pastillas específicas.
# Restricciones y Expectativas

# ¿Existen restricciones de tiempo, presupuesto o tecnología?
# 	R: 20 segundo cargando, sin limite de tiempo de uso. 

# ¿Cómo espera que sea la interfaz de uso? (simple, avanzada, web, móvil)
# 	R: full responsivo
	
# ¿Hay límites en la cantidad de datos que se almacenarán? (número
# aproximado de registros)
# 	R: No hay límites de datos almacenados.

# Regulaciones y Seguridad

# ¿Existen regulaciones legales o normativas que el sistema debe cumplir?
# (ejemplo: Ley de Protección de Datos)
# 	R: Todas las regulaciones.

# ¿Se requiere control de acceso con usuarios y contraseñas?
# R: Si, se requiere.

# ¿Debe registrarse un historial de modificaciones? (campos de auditoría)
# 	R: Si se requiere.

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
    cursor.execute("CREATE DATABASE IF NOT EXISTS Cronodosis")

    # Cambiar a la base de datos
    cursor.execute("USE Cronodosis")
    print("Base de datos 'Cronodosis' creada y seleccionada.")
    
    # Tabla: roles
    cursor.execute("""CREATE TABLE IF NOT EXISTS roles (
                id_rol INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                nombre_rol VARCHAR(50) NOT NULL CHECK (nombre_rol in ('Administrador','Usuario','Tutor')),
                descripcion_rol VARCHAR(200) NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_by INT,
                updated_by INT,
                deleted BOOLEAN DEFAULT FALSE
                );""")
    print("Tabla 'roles' creada.")
    # Tabla: usuarios
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                nombre_usuario VARCHAR(100) NOT NULL,
                correo VARCHAR(100) NOT NULL UNIQUE,
                rut VARCHAR(12) NOT NULL UNIQUE,
                contrasena VARCHAR(255) NOT NULL,
                numero_telefono VARCHAR(15),
                edad INT CHECK (edad >= 0),
                genero ENUM('Masculino', 'Femenino', 'Otro'),
                alergias TEXT,
                enfermedades_cronicas TEXT,
                frecuencia_tratamiento VARCHAR(100),
                tipo_tratamiento VARCHAR(100),
                duracion_tratamiento VARCHAR(100),
                id_rol INT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_by INT,
                updated_by INT,
                deleted BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
                );""")
    print("Tabla 'usuarios' creada.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()


