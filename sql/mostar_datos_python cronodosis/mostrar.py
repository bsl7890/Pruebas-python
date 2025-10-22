 
import os
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "CRONODOSIS",
    "port": "3306"
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)
def sp_tipo_genero_listar_activos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_tipo_genero_listar_activos")
        print("=== TIPOS DE GÉNERO ===")
        for result in cur.stored_results():
            for (id_genero, nombre_genero, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_genero:<3} | Género:{nombre_genero:<20} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_tipo_genero_listar_activos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_listar_tipo_alergias():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_tipo_alergias")
        print("=== TIPOS DE ALERGIAS ===")
        for result in cur.stored_results():
            for (id_alergia, nombre_alergia, descripcion, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_alergia:<3} | Alergia:{nombre_alergia:<30} | Descripción:{descripcion:<45} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_tipo_alergias:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_listar_personas():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_personas")
        print("=== PERSONAS ===")
        for result in cur.stored_results():
            for (id_persona, nombre, correo, rut, telefono, fecha_nacimiento, id_genero, id_alergia, enfermedades_cronicas, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_persona:<3} | Nombre:{nombre:<20} | Correo:{correo:<30} | RUT:{rut:<15} | Teléfono:{telefono:<15} | Fecha Nac.:{fecha_nacimiento} | Género ID:{id_genero} | Alergia ID:{id_alergia} | Enfermedades Crónicas:{enfermedades_cronicas:<50} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_personas:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_listar_tipo_usuario():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_tipo_usuario")
        print("=== TIPOS DE USUARIO ===")
        for result in cur.stored_results():
            for (id_tipo_u, nombre_tipo_u, descripcion_tipo_u, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_tipo_u:<3} | Tipo Usuario:{nombre_tipo_u:<20} | Descripción:{descripcion_tipo_u:<50} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_tipo_usuario:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_listar_usuarios():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_usuarios")
        print("=== USUARIOS ===")
        for result in cur.stored_results():
            for (id_usuario, nombre_usuario, password_usuario, id_persona, tipo_usuario_id, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_usuario:<3} | Usuario:{nombre_usuario:<20} | Password:{password_usuario:<20} | Persona ID:{id_persona} | Tipo Usuario ID:{tipo_usuario_id} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_usuarios:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_listar_tipo_tratamientos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_tipo_tratamientos")
        print("=== TIPOS DE TRATAMIENTOS ===")
        for result in cur.stored_results():
            for (id_tratamiento, nombre_tratamiento, descripcion, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_tratamiento:<3} | Tratamiento:{nombre_tratamiento:<30} | Descripción:{descripcion:<45} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_tipo_tratamientos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_listar_medicamentos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_medicamentos")
        print("=== MEDICAMENTOS ===")
        for result in cur.stored_results():
            for (id_medicamento, nombre_medicamento, frecuencia_tratamiento, duracion_tratamiento, usuario_id, id_tratamiento, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_medicamento:<3} | Medicamento:{nombre_medicamento:<30} | Frecuencia:{frecuencia_tratamiento:<20} | Duración:{duracion_tratamiento:<20} | Usuario ID:{usuario_id} | Tratamiento ID:{id_tratamiento} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_medicamentos:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_listar_alarmas():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_alarmas")
        print("=== ALARMAS ===")
        for result in cur.stored_results():
            for (id_alarma, hora, fecha, medicamento_id, usuario_id, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_alarma:<3} | Hora:{hora} | Fecha:{fecha} | Medicamento ID:{medicamento_id} | Usuario ID:{usuario_id} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_alarmas:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_listar_estado_pastillero():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_estado_pastillero")
        print("=== ESTADO PASTILLERO ===")
        for result in cur.stored_results():
            for (id_estado, nombre_estado, descripcion, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_estado:<3} | Estado:{nombre_estado:<20} | Descripción:{descripcion:<45} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_estado_pastillero:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
        
def sp_listar_historial_medicamentos():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_historial_medicamentos")
        print("=== HISTORIAL MEDICAMENTOS ===")
        for result in cur.stored_results():
            for (id_historial, medicamento_id, usuario_id, fecha, hora, cumplimiento_tratamiento, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_historial:<3} | Medicamento ID:{medicamento_id} | Usuario ID:{usuario_id} | Fecha:{fecha} | Hora:{hora} | Cumplimiento:{cumplimiento_tratamiento} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_historial_medicamentos:", e)
        input("Presiona Enter para continuar......")
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()
def sp_listar_pastilleros():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_pastilleros")
        print("=== PASTILLEROS ===")
        for result in cur.stored_results():
            for (id_pastillero, nombre_pastillero, usuario_id, id_estado, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_pastillero:<3} | Pastillero:{nombre_pastillero:<30} | Usuario ID:{usuario_id} | Estado ID:{id_estado} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_pastilleros:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()

def sp_listar_tutor_usuario():
    cnx = cur = None
    try:
        cnx = conectar()
        cur = cnx.cursor()
        cur.callproc("sp_listar_tutor_usuario")
        print("=== TUTOR-USUARIO ===")
        for result in cur.stored_results():
            for (id_tutor_usuario, tutor_id, usuario_id, created_at, updated_at) in result.fetchall():
                ua = updated_at if updated_at is not None else "-"
                print(f"ID:{id_tutor_usuario:<3} | Tutor ID:{tutor_id} | Usuario ID:{usuario_id} | Creado:{created_at} | Actualizado:{ua}")
        input("Presiona Enter para continuar......")
    except mysql.connector.Error as e:
        print("❌ Error en sp_listar_tutor_usuario:", e)
        input("Presiona Enter para continuar......")
        
    finally:
        if cur: cur.close()
        if cnx and cnx.is_connected(): cnx.close()



def opcion1():
    print("Opción Listar tipos de género  seleccionada.")
    sp_tipo_genero_listar_activos()
def otros_generos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_tipo_genero = {
    1: opcion1,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_tipo_genero(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_alergias():
    print("Opción Listar tipos de alergias  seleccionada.")
    sp_listar_tipo_alergias()

def otros_alergias():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_tipo_alergias = {
    1: opcion1_alergias,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_tipo_alergias(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_personas():
    print("Opción Listar personas seleccionada.")
    sp_listar_personas()
def otros_personas():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_personas = {
    1: opcion1_personas,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_personas(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_tipo_usuario():
    print("Opción Listar tipos de usuario seleccionada.")
    sp_listar_tipo_usuario()
def otros_tipo_usuario():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_tipo_usuario = {
    1: opcion1_tipo_usuario,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_tipo_usuario(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_usuarios():
    print("Opción Listar usuarios seleccionada.")
    sp_listar_usuarios()
def otros_usuarios():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_usuarios = {
    1: opcion1_usuarios,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_usuarios(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
        
def opcion1_tipo_tratamientos():
    print("Opción Listar tipos de tratamientos seleccionada.")
    sp_listar_tipo_tratamientos()
def otros_tipo_tratamientos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_tipo_tratamientos = {
    1: opcion1_tipo_tratamientos,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_tipo_tratamientos(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_medicamentos():
    print("Opción Listar medicamentos seleccionada.")
    sp_listar_medicamentos()

def otros_medicamentos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_medicamentos = {
    1: opcion1_medicamentos,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_medicamentos(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_alarmas():
    print("Opción Listar alarmas seleccionada.")
    sp_listar_alarmas()

def otros_alarmas():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_alarmas = {
    1: opcion1_alarmas,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_alarmas(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_estado_pastillero():
    print("Opción Listar estado pastillero seleccionada.")
    sp_listar_estado_pastillero()

def otros_estado_pastillero():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_estado_pastillero = {
    1: opcion1_estado_pastillero,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_estado_pastillero(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_historial_medicamentos():
    print("Opción Listar historial medicamentos seleccionada.")
    sp_listar_historial_medicamentos()
def otros_historial_medicamentos():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_historial_medicamentos = {
    1: opcion1_historial_medicamentos,
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
            print("|------------------------------------------|")
            print("|       Menú Historial Medicamentos        |")
            print("|------------------------------------------|")
            print("|  1 - Listar historial medicamentos       |")
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_historial_medicamentos(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_pastilleros():
    print("Opción Listar pastilleros seleccionada.")
    sp_listar_pastilleros()
def otros_pastilleros():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_pastilleros = {
    1: opcion1_pastilleros,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
                break
            opcion_seleccionada_pastilleros(opcion)
        except ValueError:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar......")
            continue
def opcion1_tutor_usuario():
    print("Opción Listar tutor-usuario seleccionada.")
    sp_listar_tutor_usuario()

def otros_tutor_usuario():
    print("Por favor seleccione una opción válida.")
    input("Presiona Enter para continuar......")
opciones_menu_tutor_usuario = {
    1: opcion1_tutor_usuario,
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
            print("|  2 - Volver al menú principal            |")
            print("|------------------------------------------|")
            opcion = int(input("Selecciona una opción: ").strip())
            if opcion == 2:
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
            