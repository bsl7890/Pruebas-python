import os
import mysql.connector
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "CRONODOSIS",
    "port": "3306"
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)

# ========================================
# FUNCIONES TIPO GÉNERO
# ========================================
def sp_tipo_genero_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_genero_listar_activos")
        print("=== TIPOS DE GÉNERO ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_genero, nombre_genero, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_genero:<3} | Género:{nombre_genero:<20} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_tipo_genero_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_tipo_genero_insertar():
    cnx = cur = None
    try:
        nombre = input("Ingrese el nombre del género: ").strip()
        created_by = int(input("Ingrese el ID del usuario que crea el registro: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_genero_insertar", [nombre, created_by])
        cnx.commit()
        print("✅ Tipo de género insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar tipo de género:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: El ID debe ser un número.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# Borrado logico (actualiza el campo deleted a True sin eliminar el registro físicamente de la base de datos ) TRUE = 1 FALSE = 0
def sp_tipo_genero_borrado_logico():
    cnx = cur = None
    try:
        id_genero = int(input("Ingrese el ID del género a eliminar: ").strip())
        updated_by = int(input("Ingrese el ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_genero_borrado_logico", [id_genero, updated_by])
        cnx.commit()
        print("✅ Tipo de género eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar tipo de género:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES TIPO ALERGIAS
# ========================================
def sp_tipo_alergias_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_alergias_listar_activos")
        print("=== TIPOS DE ALERGIAS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_alergia, nombre_alergia, descripcion, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_alergia:<3} | Alergia:{nombre_alergia:<30} | Descripción:{descripcion:<50} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
                    
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_tipo_alergias_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_tipo_alergias_insertar():
    cnx = cur = None
    try:
        nombre = input("Ingrese el nombre de la alergia: ").strip()
        descripcion = input("Ingrese la descripción: ").strip()
        created_by = int(input("Ingrese el ID del usuario que crea el registro: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_alergias_insertar", [nombre, descripcion, created_by])
        cnx.commit()
        print("✅ Tipo de alergia insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar tipo de alergia:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: El ID debe ser un número.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_tipo_alergias_borrado_logico():
    cnx = cur = None
    try:
        id_alergia = int(input("Ingrese el ID de la alergia a eliminar: ").strip())
        updated_by = int(input("Ingrese el ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_alergias_borrado_logico", [id_alergia, updated_by])
        cnx.commit()
        print("✅ Tipo de alergia eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar tipo de alergia:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES PERSONAS
# ========================================
def sp_personas_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_personas_listar_activos")
        print("=== PERSONAS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_persona, nombre, correo, rut, telefono, fecha_nacimiento, id_genero, id_alergia, enfermedades_cronicas, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_persona:<3} | Nombre:{nombre:<20} | Correo:{correo:<30} | RUT:{rut:<15} | Tel:{telefono:<15} | F.Nac:{fecha_nacimiento} | Género ID:{id_genero} | Alergia ID:{id_alergia} | Enfermedades:{enfermedades_cronicas} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_personas_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_personas_insertar():
    cnx = cur = None
    try:
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()
        rut = input("RUT: ").strip()
        telefono = input("Teléfono: ").strip()
        fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()
        id_genero = int(input("ID Género: ").strip())
        id_alergia_str = input("ID Alergia (deje vacío si no tiene): ").strip()
        id_alergia = int(id_alergia_str) if id_alergia_str else None
        enfermedades = input("Enfermedades crónicas (opcional): ").strip() or None
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_personas_insertar", [nombre, correo, rut, telefono, fecha_nac, id_genero, id_alergia, enfermedades, created_by])
        cnx.commit()
        print("✅ Persona insertada correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar persona:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Verifique los datos numéricos.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_personas_borrado_logico():
    cnx = cur = None
    try:
        id_persona = int(input("Ingrese el ID de la persona a eliminar: ").strip())
        updated_by = int(input("Ingrese el ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_personas_borrado_logico", [id_persona, updated_by])
        cnx.commit()
        print("✅ Persona eliminada correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar persona:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES TIPO USUARIO
# ========================================
def sp_tipo_usuario_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_usuario_listar_activos")
        print("=== TIPOS DE USUARIO ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_tipo_u, nombre_tipo_u, descripcion_tipo_u, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_tipo_u:<3} | Tipo:{nombre_tipo_u:<20} | Descripción:{descripcion_tipo_u:<50} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_tipo_usuario_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_tipo_usuario_insertar():
    cnx = cur = None
    try:
        nombre = input("Nombre del tipo de usuario: ").strip()
        descripcion = input("Descripción: ").strip()
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_usuario_insertar", [nombre, descripcion, created_by])
        cnx.commit()
        print("✅ Tipo de usuario insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar tipo de usuario:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: El ID debe ser un número.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_tipo_usuario_borrado_logico():
    cnx = cur = None
    try:
        id_tipo_u = int(input("ID del tipo de usuario a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_usuario_borrado_logico", [id_tipo_u, updated_by])
        cnx.commit()
        print("✅ Tipo de usuario eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar tipo de usuario:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES USUARIOS
# ========================================
def sp_usuarios_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_usuarios_listar_activos")
        print("=== USUARIOS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_usuario, nombre_usuario, password_usuario, id_persona, tipo_usuario_id, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_usuario:<3} | Usuario:{nombre_usuario:<20} | contrasena:{password_usuario} | Persona ID:{id_persona} | Tipo:{tipo_usuario_id} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_usuarios_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_usuarios_insertar():
    cnx = cur = None
    try:
        nombre_usuario = input("Nombre de usuario: ").strip()
        password = input("Contraseña: ").strip()
        id_persona = int(input("ID de la persona: ").strip())
        tipo_usuario_id = int(input("ID del tipo de usuario: ").strip())
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_usuarios_insertar", [nombre_usuario, password, id_persona, tipo_usuario_id, created_by])
        cnx.commit()
        print("✅ Usuario insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar usuario:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_usuarios_borrado_logico():
    cnx = cur = None
    try:
        id_usuario = int(input("ID del usuario a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_usuarios_borrado_logico", [id_usuario, updated_by])
        cnx.commit()
        print("✅ Usuario eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar usuario:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES TIPO TRATAMIENTOS
# ========================================
def sp_tipo_tratamientos_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_tratamientos_listar_activos")
        print("=== TIPOS DE TRATAMIENTOS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_tratamiento, nombre_tratamiento, descripcion, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_tratamiento:<3} | Tratamiento:{nombre_tratamiento:<30} | Desc:{descripcion:<45} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_tipo_tratamientos_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_tipo_tratamientos_insertar():
    cnx = cur = None
    try:
        nombre = input("Nombre del tratamiento: ").strip()
        descripcion = input("Descripción: ").strip()
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_tratamientos_insertar", [nombre, descripcion, created_by])
        cnx.commit()
        print("✅ Tipo de tratamiento insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar tipo de tratamiento:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: El ID debe ser un número.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_tipo_tratamientos_borrado_logico():
    cnx = cur = None
    try:
        id_tratamiento = int(input("ID del tratamiento a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_tratamientos_borrado_logico", [id_tratamiento, updated_by])
        cnx.commit()
        print("✅ Tipo de tratamiento eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar tipo de tratamiento:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES MEDICAMENTOS
# ========================================
def sp_medicamentos_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_medicamentos_listar_activos")
        print("=== MEDICAMENTOS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_medicamento, nombre_medicamento, frecuencia_tratamiento, duracion_tratamiento, usuario_id, id_tratamiento, created_at, updated_at, created_by, updated_by, deleted = row
                    print(f"ID:{id_medicamento:<3} | Med:{nombre_medicamento:<30} | Frec:{frecuencia_tratamiento:<20} | Durac:{duracion_tratamiento:<15} | Usuario ID:{usuario_id} | Tratamiento ID:{id_tratamiento} | Creado:{created_at} | Actualizado:{updated_at} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_medicamentos_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_medicamentos_insertar():
    cnx = cur = None
    try:
        nombre = input("Nombre del medicamento: ").strip()
        frecuencia = input("Frecuencia (ej: Cada 8 horas): ").strip()
        duracion = input("Duración (ej: 7 días): ").strip()
        usuario_id = int(input("ID del usuario: ").strip())
        id_tratamiento = int(input("ID del tipo de tratamiento: ").strip())
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_medicamentos_insertar", [nombre, frecuencia, duracion, usuario_id, id_tratamiento, created_by])
        cnx.commit()
        print("✅ Medicamento insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar medicamento:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_medicamentos_borrado_logico():
    cnx = cur = None
    try:
        id_medicamento = int(input("ID del medicamento a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_medicamentos_borrado_logico", [id_medicamento, updated_by])
        cnx.commit()
        print("✅ Medicamento eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar medicamento:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES ALARMAS
# ========================================
def sp_alarmas_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_alarmas_listar_activos")
        print("=== ALARMAS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_alarma, hora, fecha, medicamento_id, usuario_id, created_at, updated_at, created_by, updated_by, deleted = row
                    print(f"ID:{id_alarma:<3} | Hora:{hora} | Fecha:{fecha} | Med ID:{medicamento_id} | Usuario:{usuario_id} | creado:{created_at} | actualizado:{updated_at} | creado por:{created_by} | actualizado por:{updated_by} | eliminado:{deleted} ")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_alarmas_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_alarmas_insertar():
    cnx = cur = None
    try:
        hora = input("Hora (HH:MM:SS): ").strip()
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        medicamento_id = int(input("ID del medicamento: ").strip())
        usuario_id = int(input("ID del usuario: ").strip())
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_alarmas_insertar", [hora, fecha, medicamento_id, usuario_id, created_by])
        cnx.commit()
        print("✅ Alarma insertada correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar alarma:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_alarmas_borrado_logico():
    cnx = cur = None
    try:
        id_alarma = int(input("ID de la alarma a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_alarmas_borrado_logico", [id_alarma, updated_by])
        cnx.commit()
        print("✅ Alarma eliminada correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar alarma:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# ========================================
# FUNCIONES ESTADO PASTILLERO
# ========================================

def sp_estado_pastillero_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_estado_pastillero_listar_activos")
        print("=== ESTADO PASTILLERO ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_estado, nombre_estado, descripcion, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_estado:<3} | Estado:{nombre_estado:<20} | Descripción:{descripcion:<45} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_estado_pastillero_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_estado_pastillero_insertar():
    cnx = cur = None
    try:
        nombre = input("Nombre del estado del pastillero: ").strip()
        descripcion = input("Descripción: ").strip()
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_estado_pastillero_insertar", [nombre, descripcion, created_by])
        cnx.commit()
        print("✅ Estado del pastillero insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar estado del pastillero:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: El ID debe ser un número.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_estado_pastillero_borrado_logico():
    cnx = cur = None
    try:
        id_estado = int(input("ID del estado del pastillero a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_estado_pastillero_borrado_logico", [id_estado, updated_by])
        cnx.commit()
        print("✅ Estado del pastillero eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar estado del pastillero:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
# ========================================
# FUNCIONES HISTORIAL MEDICAMENTOS
# ========================================

def sp_historial_medicamentos_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_historial_medicamentos_listar_activos")
        print("=== HISTORIAL MEDICAMENTOS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_historial, medicamento_id, usuario_id, fecha, hora, cumplimiento_tratamiento, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_historial:<3} | Medicamento ID:{medicamento_id} | Usuario ID:{usuario_id} | Fecha:{fecha} | Hora:{hora} | Cumplimiento:{cumplimiento_tratamiento} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_historial_medicamentos_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_historial_medicamentos_insertar():
    cnx = cur = None
    try:
        medicamento_id = int(input("ID del medicamento: ").strip())
        usuario_id = int(input("ID del usuario: ").strip())
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        hora = input("Hora (HH:MM:SS): ").strip()
        cumplimiento = input("Cumplimiento del tratamiento (Sí/No): ").strip()
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_historial_medicamentos_insertar", [medicamento_id, usuario_id, fecha, hora, cumplimiento, created_by])
        cnx.commit()
        print("✅ Historial de medicamento insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar historial de medicamento:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_historial_medicamentos_borrado_logico():
    cnx = cur = None
    try:
        id_historial = int(input("ID del historial de medicamento a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_historial_medicamentos_borrado_logico", [id_historial, updated_by])
        cnx.commit()
        print("✅ Historial de medicamento eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar historial de medicamento:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
# ========================================
# FUNCIONES PASTILLEROS
# ========================================

def sp_pastilleros_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_pastilleros_listar_activos")
        print("=== PASTILLEROS ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_pastillero, nombre_pastillero, usuario_id, id_estado, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_pastillero:<3} | Pastillero:{nombre_pastillero:<30} | Usuario ID:{usuario_id} | Estado ID:{id_estado} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_pastilleros_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_pastilleros_insertar():
    cnx = cur = None
    try:
        nombre = input("Nombre del pastillero: ").strip()
        usuario_id = int(input("ID del usuario: ").strip())
        id_estado = int(input("ID del estado del pastillero: ").strip())
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_pastilleros_insertar", [nombre, usuario_id, id_estado, created_by])
        cnx.commit()
        print("✅ Pastillero insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar pastillero:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_pastilleros_borrado_logico():
    cnx = cur = None
    try:
        id_pastillero = int(input("ID del pastillero a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_pastilleros_borrado_logico", [id_pastillero, updated_by])
        cnx.commit()
        print("✅ Pastillero eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar pastillero:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
# ========================================
# FUNCIONES TUTOR-USUARIO
# ========================================

def sp_tutor_usuario_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tutor_usuario_listar_activos")
        print("=== TUTOR-USUARIO ===")
        
        resultados_encontrados = False
        for result in cur.stored_results():
            rows = result.fetchall()
            if rows:
                resultados_encontrados = True
                for row in rows:
                    id_tutor_usuario, tutor_id, usuario_id, created_at, updated_at, created_by, updated_by, deleted = row
                    ua = updated_at if updated_at is not None else "-"
                    print(f"ID:{id_tutor_usuario:<3} | Tutor ID:{tutor_id} | Usuario ID:{usuario_id} | Creado:{created_at} | Actualizado:{ua} | Creado por:{created_by} | Actualizado por:{updated_by} | Eliminado:{deleted}")
        
        if not resultados_encontrados:
            print("No hay registros para mostrar.")
            
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error en sp_tutor_usuario_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_tutor_usuario_insertar():
    cnx = cur = None
    try:
        tutor_id = int(input("ID del tutor: ").strip())
        usuario_id = int(input("ID del usuario: ").strip())
        created_by = int(input("ID del usuario que crea: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tutor_usuario_insertar", [tutor_id, usuario_id, created_by])
        cnx.commit()
        print("✅ Tutor-Usuario insertado correctamente.")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al insertar Tutor-Usuario:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_tutor_usuario_borrado_logico():
    cnx = cur = None
    try:
        id_tutor_usuario = int(input("ID del Tutor-Usuario a eliminar: ").strip())
        updated_by = int(input("ID del usuario que realiza la eliminación: ").strip())
        
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tutor_usuario_borrado_logico", [id_tutor_usuario, updated_by])
        cnx.commit()
        print("✅ Tutor-Usuario eliminado correctamente (borrado lógico).")
        input("Presiona Enter para continuar......")
        
    except mysql.connector.Error as e:
        print("❌ Error al eliminar Tutor-Usuario:", e)
        if cnx:
            cnx.rollback()
        input("Presiona Enter para continuar......")
    except ValueError:
        print("❌ Error: Los IDs deben ser números.")
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

# === FUNCIONES DE MENÚ ===

def opcion1():
    print("Opción Listar tipos de género seleccionada.")
    sp_tipo_genero_listar_activos()
def opcios_2():
    print("Opción Insertar nuevo tipo de género seleccionada.")
    sp_tipo_genero_insertar()
def opcios_3():
    print("Opción Eliminar tipo de género seleccionada.")
    sp_tipo_genero_borrado_logico()
    
def otros_generos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")

opciones_menu_tipo_genero = {
    1: opcion1,
    2: opcios_2,
    3: opcios_3,
}

def opcion_seleccionada_tipo_genero(opcion, otros=False):
    funcion = opciones_menu_tipo_genero.get(opcion if not otros else None, otros_generos)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")

def menu_tipo_genero():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|       Menú Tipo de Género                |")
            print("|------------------------------------------|")
            print("|  1 - Listar tipos de género              |")
            print("|  2 - Insertar nuevo tipo de género       |")
            print("|  3 - Eliminar tipo de género             |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_tipo_genero(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

def opcion1_alergias():
    print("Opción Listar tipos de alergias seleccionada.")
    sp_tipo_alergias_listar_activos()
def opcion2_alergias():
    print("Opción Insertar nuevo tipo de alergia seleccionada.")
    sp_tipo_alergias_insertar()
def opcion3_alergias():
    print("Opción Eliminar tipo de alergia seleccionada.")
    sp_tipo_alergias_borrado_logico()
def otros_alergias():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")

opciones_menu_tipo_alergias = {
    1: opcion1_alergias,
    2: opcion2_alergias,
    3: opcion3_alergias,
}

def opcion_seleccionada_tipo_alergias(opcion, otros=False):
    funcion = opciones_menu_tipo_alergias.get(opcion if not otros else None, otros_alergias)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")

def menu_tipo_alergias():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|       Menú Tipo de Alergias              |")
            print("|------------------------------------------|")
            print("|  1 - Listar tipos de alergias            |")
            print("|  2 - Insertar nuevo tipo de alergia      |")
            print("|  3 - Eliminar tipo de alergia            |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_tipo_alergias(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

def opcion1_personas():
    print("Opción Listar personas seleccionada.")
    sp_personas_listar_activos()
def opcion2_personas():
    print("Opción Insertar nueva persona seleccionada.")
    sp_personas_insertar()
def opcion3_personas():
    print("Opción Eliminar persona seleccionada.")
    sp_personas_borrado_logico()
def otros_personas():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")

opciones_menu_personas = {
    1: opcion1_personas,
    2: opcion2_personas,
    3: opcion3_personas,
}

def opcion_seleccionada_personas(opcion, otros=False):
    funcion = opciones_menu_personas.get(opcion if not otros else None, otros_personas)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")

def menu_personas():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|           Menú Personas                  |")
            print("|------------------------------------------|")
            print("|  1 - Listar personas                     |")
            print("|  2 - Insertar nueva persona              |")
            print("|  3 - Eliminar persona                    |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_personas(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

def opcion1_tipo_usuario():
    print("Opción Listar tipos de usuario seleccionada.")
    sp_tipo_usuario_listar_activos()
def opcion2_tipo_usuario():
    print("Opción Insertar nuevo tipo de usuario seleccionada.")
    sp_tipo_usuario_insertar()
def opcion3_tipo_usuario():
    print("Opción Eliminar tipo de usuario seleccionada.")
    sp_tipo_usuario_borrado_logico()
def otros_tipo_usuario():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")

opciones_menu_tipo_usuario = {
    1: opcion1_tipo_usuario,
    2: opcion2_tipo_usuario,
    3: opcion3_tipo_usuario,
}

def opcion_seleccionada_tipo_usuario(opcion, otros=False):
    funcion = opciones_menu_tipo_usuario.get(opcion if not otros else None, otros_tipo_usuario)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")

def menu_tipo_usuario():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|        Menú Tipo de Usuario              |")
            print("|------------------------------------------|")
            print("|  1 - Listar tipos de usuario             |")
            print("|  2 - Insertar nuevo tipo de usuario      |")
            print("|  3 - Eliminar tipo de usuario            |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_tipo_usuario(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

def opcion1_usuarios():
    print("Opción Listar usuarios seleccionada.")
    sp_usuarios_listar_activos()
def opcion2_usuarios():
    print("Opción Insertar nuevo usuario seleccionada.")
    sp_usuarios_insertar()
def opcion3_usuarios():
    print("Opción Eliminar usuario seleccionada.")
    sp_usuarios_borrado_logico()
def otros_usuarios():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")

opciones_menu_usuarios = {
    1: opcion1_usuarios,
    2: opcion2_usuarios,
    3: opcion3_usuarios,
}

def opcion_seleccionada_usuarios(opcion, otros=False):
    funcion = opciones_menu_usuarios.get(opcion if not otros else None, otros_usuarios)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")

def menu_usuarios():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|            Menú Usuarios                 |")
            print("|------------------------------------------|")
            print("|  1 - Listar usuarios                     |")
            print("|  2 - Insertar nuevo usuario              |")
            print("|  3 - Eliminar usuario                    |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_usuarios(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

def opcion1_tipo_tratamientos():
    print("Opción Listar tipos de tratamientos seleccionada.")
    sp_tipo_tratamientos_listar_activos()
def opcion2_tipo_tratamientos():
    print("Opción Insertar nuevo tipo de tratamiento seleccionada.")
    sp_tipo_tratamientos_insertar()
def opcion3_tipo_tratamientos():
    print("Opción Eliminar tipo de tratamiento seleccionada.")
    sp_tipo_tratamientos_borrado_logico()
def otros_tipo_tratamientos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")

opciones_menu_tipo_tratamientos = {
    1: opcion1_tipo_tratamientos,
    2: opcion2_tipo_tratamientos,
    3: opcion3_tipo_tratamientos,
}

def opcion_seleccionada_tipo_tratamientos(opcion, otros=False):
    funcion = opciones_menu_tipo_tratamientos.get(opcion if not otros else None, otros_tipo_tratamientos)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")

def menu_tipo_tratamientos():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|       Menú Tipo de Tratamientos          |")
            print("|------------------------------------------|")
            print("|  1 - Listar tipos de tratamientos        |")
            print("|  2 - Insertar nuevo tipo de tratamiento  |")
            print("|  3 - Eliminar tipo de tratamiento        |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_tipo_tratamientos(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

def opcion1_medicamentos():
    print("Opción Listar medicamentos seleccionada.")
    sp_medicamentos_listar_activos()
def opcion2_medicamentos():
    print("Opción Insertar nuevo medicamento seleccionada.")
    sp_medicamentos_insertar()
def opcion3_medicamentos():
    print("Opción Eliminar medicamento seleccionada.")
    sp_medicamentos_borrado_logico()

def otros_medicamentos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")

opciones_menu_medicamentos = {
    1: opcion1_medicamentos,
    2: opcion2_medicamentos,
    3: opcion3_medicamentos,
}

def opcion_seleccionada_medicamentos(opcion, otros=False):
    funcion = opciones_menu_medicamentos.get(opcion if not otros else None, otros_medicamentos)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")

def menu_medicamentos():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|           Menú Medicamentos              |")
            print("|------------------------------------------|")
            print("|  1 - Listar medicamentos                 |")
            print("|  2 - Insertar nuevo medicamento          |")
            print("|  3 - Eliminar medicamento                |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_medicamentos(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

def opcion1_alarmas():
    print("Opción Listar alarmas seleccionada.")
    sp_alarmas_listar_activos()
def opcion2_alarmas():
    print("Opción Insertar nuevo alarma seleccionada.")
    sp_alarmas_insertar()
def opcion3_alarmas():
    print("Opción Eliminar alarma seleccionada.")
    sp_alarmas_borrado_logico()

def otros_alarmas():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_alarmas = {
    1: opcion1_alarmas,
    2: opcion2_alarmas,
    3: opcion3_alarmas,
}
def opcion_seleccionada_alarmas(opcion, otros=False):
    funcion = opciones_menu_alarmas.get(opcion if not otros else None, otros_alarmas)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")
def menu_alarmas():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|             Menú Alarmas                 |")
            print("|------------------------------------------|")
            print("|  1 - Listar alarmas                      |")
            print("|  2 - Insertar nuevo alarma               |")
            print("|  3 - Eliminar alarma                     |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_alarmas(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_estado_pastillero():
    print("Opción Listar estado pastillero seleccionada.")
    sp_estado_pastillero_listar_activos()
def opcion2_estado_pastillero():
    print("Opción Insertar nuevo estado pastillero seleccionada.")
    sp_estado_pastillero_insertar()
def opcion3_estado_pastillero():
    print("Opción Eliminar estado pastillero seleccionada.")
    sp_estado_pastillero_borrado_logico()

def otros_estado_pastillero():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_estado_pastillero = {
    1: opcion1_estado_pastillero,
    2: opcion2_estado_pastillero,
    3: opcion3_estado_pastillero,
    }
def opcion_seleccionada_estado_pastillero(opcion, otros=False):
    funcion = opciones_menu_estado_pastillero.get(opcion if not otros else None, otros_estado_pastillero)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")
def menu_estado_pastillero():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|        Menú Estado Pastillero            |")
            print("|------------------------------------------|")
            print("|  1 - Listar estado pastillero            |")
            print("|  2 - Insertar nuevo estado pastillero    |")
            print("|  3 - Eliminar estado pastillero          |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_estado_pastillero(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_historial_medicamentos():
    print("Opción Listar historial medicamentos seleccionada.")
    sp_historial_medicamentos_listar_activos()
def opcion2_historial_medicamentos():
    print("Opción Insertar nuevo historial medicamento seleccionada.")
    sp_historial_medicamentos_insertar()
def opcion3_historial_medicamentos():
    print("Opción Eliminar historial medicamento seleccionada.")
    sp_historial_medicamentos_borrado_logico()
def otros_historial_medicamentos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_historial_medicamentos = {
    1: opcion1_historial_medicamentos,
    2: opcion2_historial_medicamentos,
    3: opcion3_historial_medicamentos,
}
def opcion_seleccionada_historial_medicamentos(opcion, otros=False):
    funcion = opciones_menu_historial_medicamentos.get(opcion if not otros else None, otros_historial_medicamentos)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")
def menu_historial_medicamentos():
    while True:
        try:
            os.system("cls")
            print("|-------------------------------------------|")
            print("|       Menú Historial Medicamentos         |")
            print("|-------------------------------------------|")
            print("|  1 - Listar historial medicamentos        |")
            print("|  2 - Insertar nuevo historial medicamento |")
            print("|  3 - Eliminar historial medicamento       |")
            print("|  4 - Volver al menú principal             |")
            print("|-------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_historial_medicamentos(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_pastilleros():
    print("Opción Listar pastilleros seleccionada.")
    sp_pastilleros_listar_activos()
def opcion2_pastilleros():
    print("Opción Insertar nuevo pastillero seleccionada.")
    sp_pastilleros_insertar()
def opcion3_pastilleros():
    print("Opción Eliminar pastillero seleccionada.")
    sp_pastilleros_borrado_logico()
def otros_pastilleros():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_pastilleros = {
    1: opcion1_pastilleros,
    2: opcion2_pastilleros,
    3: opcion3_pastilleros,
}
def opcion_seleccionada_pastilleros(opcion, otros=False):
    funcion = opciones_menu_pastilleros.get(opcion if not otros else None, otros_pastilleros)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")
def menu_pastilleros():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|           Menú Pastilleros               |")
            print("|------------------------------------------|")
            print("|  1 - Listar pastilleros                  |")
            print("|  2 - Insertar nuevo pastillero           |")
            print("|  3 - Eliminar pastillero                 |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_pastilleros(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_tutor_usuario():
    print("Opción Listar tutor-usuario seleccionada.")
    sp_tutor_usuario_listar_activos()
def opcion2_tutor_usuario():
    print("Opción Insertar nuevo tutor-usuario seleccionada.")
    sp_tutor_usuario_insertar()
def opcion3_tutor_usuario():
    print("Opción Eliminar tutor-usuario seleccionada.")
    sp_tutor_usuario_borrado_logico()
def otros_tutor_usuario():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_tutor_usuario = {
    1: opcion1_tutor_usuario,
    2: opcion2_tutor_usuario,
    3: opcion3_tutor_usuario,
}
def opcion_seleccionada_tutor_usuario(opcion, otros=False):
    funcion = opciones_menu_tutor_usuario.get(opcion if not otros else None, otros_tutor_usuario)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")
def menu_tutor_usuario():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|          Menú Tutor-Usuario              |")
            print("|------------------------------------------|")
            print("|  1 - Listar tutor-usuario                |")
            print("|  2 - Insertar nuevo tutor-usuario        |")
            print("|  3 - Eliminar tutor-usuario              |")
            print("|  4 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 4:
                break
            opcion_seleccionada_tutor_usuario(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
        
        
def otros_menu_principal():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")  
opcion_seleccionada_menu_principal = {
    1: menu_tipo_genero,
    2: menu_tipo_alergias,
    3: menu_personas,
    4: menu_tipo_usuario,
    5: menu_usuarios,
    6: menu_tipo_tratamientos,
    7: menu_medicamentos,
    8: menu_alarmas,
    9: menu_estado_pastillero,
    10: menu_historial_medicamentos,
    11: menu_pastilleros,
    12: menu_tutor_usuario
}
def opcion_seleccionada_menu(opcion, otros=False):
    funcion = opcion_seleccionada_menu_principal.get(opcion if not otros else None, otros_menu_principal)
    if funcion:
        funcion()
    else:
        print("❌ Opción no válida. Intenta nuevamente.")
        input("Presiona Enter para continuar......")
    
def menu_principal():
    while True:
        try:
            os.system("cls")
            print("|------------------------------------------|")
            print("|          Menú Principal                  |")
            print("|------------------------------------------|")
            print("|  1 - Tipo de Género                      |")
            print("|  2 - Tipo de Alergias                    |")
            print("|  3 - Personas                            |")
            print("|  4 - Tipo de Usuario                     |")
            print("|  5 - Usuarios                            |")
            print("|  6 - Tipo de Tratamientos                |")
            print("|  7 - Medicamentos                        |")
            print("|  8 - Alarmas                             |")
            print("|  9 - Estado Pastillero                   |")
            print("| 10 - Historial Medicamentos              |")
            print("| 11 - Pastilleros                         |")
            print("| 12 - Tutor-Usuario                       |")
            print("| 13 - Salir                               |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 13:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            opcion_seleccionada_menu(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue

if __name__ == "__main__":
    menu_principal()
            