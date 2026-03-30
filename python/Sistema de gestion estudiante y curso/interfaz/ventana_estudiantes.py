import customtkinter as ctk
from tkinter import messagebox, ttk
import json
import os

class VentanaEstudiantes(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.padre = padre
        
        self.title("🎓 Gestión de Estudiantes")
        self.geometry("900x650")
        self.resizable(False, False)
        
        # Configuración de rutas y datos
        self.directorio = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.archivo_datos = os.path.join(self.directorio, "datos_estudiantes.json")
        self.estudiantes = self.cargar_datos()
        
        # Configurar cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
        self.crear_interfaz()
        
    def cargar_datos(self):
        """Carga los estudiantes desde JSON"""
        try:
            with open(self.archivo_datos, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
            
    def guardar_datos(self):
        """Guarda los estudiantes en JSON"""
        with open(self.archivo_datos, "w", encoding="utf-8") as f:
            json.dump(self.estudiantes, f, indent=2, ensure_ascii=False)
            
    def cerrar_ventana(self):
        """Cierra esta ventana modal"""
        self.destroy()
            
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz"""
        
        # Frame superior
        frame_superior = ctk.CTkFrame(self)
        frame_superior.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(frame_superior, text="🎓 Gestión de Estudiantes", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=10)
        
        ctk.CTkButton(frame_superior, text="⬅ Volver", width=100, 
                     command=self.cerrar_ventana).pack(side="right", padx=10)
        
        # Frame de controles
        frame_controles = ctk.CTkFrame(self)
        frame_controles.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkButton(frame_controles, text="➕ Agregar", width=120, fg_color="#2E86AB",
                     command=self.abrir_formulario_agregar).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="✏️ Editar", width=120, fg_color="#F18F01",
                     command=self.editar_estudiante).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="🗑️ Eliminar", width=120, fg_color="#C73E1D",
                     command=self.eliminar_estudiante).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="🔄 Refrescar", width=120,
                     command=self.refrescar_tabla).pack(side="left", padx=5)
        
        # Buscador
        ctk.CTkLabel(frame_controles, text="🔍 Buscar:").pack(side="left", padx=(20, 5))
        self.entry_buscar = ctk.CTkEntry(frame_controles, width=200, placeholder_text="Nombre")
        self.entry_buscar.pack(side="left", padx=5)
        self.entry_buscar.bind("<KeyRelease>", lambda e: self.buscar_estudiante())
        
        # Tabla de estudiantes
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
        
        style = ttk.Style()
        style.theme_use("clam")
        
        columns = ("id", "nombre", "edad", "curso")
        self.tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings", height=15)
        
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("edad", text="Edad")
        self.tabla.heading("curso", text="Curso")
        
        self.tabla.column("id", width=80, anchor="center")
        self.tabla.column("nombre", width=300, anchor="w")
        self.tabla.column("edad", width=80, anchor="center")
        self.tabla.column("curso", width=200, anchor="w")
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.label_total = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.label_total.pack(pady=10)
        
        self.refrescar_tabla()
        
    def refrescar_tabla(self):
        """Refresca la tabla con los datos actuales"""
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for est in self.estudiantes:
            self.tabla.insert("", "end", values=(est.get("id"), est.get("nombre"), 
                                                  est.get("edad"), est.get("curso")))
        self.label_total.configure(text=f"📊 Total: {len(self.estudiantes)} estudiante(s)")
        
    def abrir_formulario_agregar(self):
        """Abre el formulario para agregar estudiante"""
        FormularioEstudiante(self, self.agregar_estudiante)
        
    def agregar_estudiante(self, datos):
        """Agrega un nuevo estudiante"""
        nuevo_id = max([e.get("id", 0) for e in self.estudiantes], default=0) + 1
        self.estudiantes.append({"id": nuevo_id, **datos})
        self.guardar_datos()
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", "✅ Estudiante agregado correctamente")
        
    def editar_estudiante(self):
        """Edita un estudiante seleccionado"""
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "⚠️ Selecciona un estudiante")
            return
        estudiante = next((e for e in self.estudiantes if e["id"] == self.tabla.item(seleccion[0])["values"][0]), None)
        if estudiante:
            FormularioEstudiante(self, self.actualizar_estudiante, estudiante)
        
    def actualizar_estudiante(self, datos):
        """Actualiza un estudiante existente"""
        for i, est in enumerate(self.estudiantes):
            if est["id"] == datos["id"]:
                self.estudiantes[i] = datos
                break
        self.guardar_datos()
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", "✅ Estudiante actualizado")
        
    def eliminar_estudiante(self):
        """Elimina un estudiante seleccionado"""
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "⚠️ Selecciona un estudiante")
            return
        id_eliminar = self.tabla.item(seleccion[0])["values"][0]
        if messagebox.askyesno("Confirmar", f"¿Eliminar estudiante ID {id_eliminar}?"):
            self.estudiantes = [e for e in self.estudiantes if e["id"] != id_eliminar]
            self.guardar_datos()
            self.refrescar_tabla()
            messagebox.showinfo("Éxito", "🗑️ Estudiante eliminado")
            
    def buscar_estudiante(self):
        """Busca estudiantes por nombre"""
        texto = self.entry_buscar.get().lower()
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for est in self.estudiantes:
            if texto in est.get("nombre", "").lower():
                self.tabla.insert("", "end", values=(est["id"], est["nombre"], est["edad"], est["curso"]))


class FormularioEstudiante(ctk.CTkToplevel):
    """Formulario modal para agregar/editar estudiantes"""
    
    def __init__(self, padre, callback, estudiante=None):
        super().__init__(padre)
        self.callback = callback
        self.estudiante = estudiante
        self.title("✏️ Agregar Estudiante" if not estudiante else "✏️ Editar Estudiante")
        self.geometry("400x350")
        self.resizable(False, False)
        self.transient(padre)
        self.grab_set()
        self.crear_formulario()
        
    def crear_formulario(self):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Nombre:").pack(anchor="w", pady=(10, 5))
        self.entry_nombre = ctk.CTkEntry(frame, width=300)
        self.entry_nombre.pack()
        
        ctk.CTkLabel(frame, text="Edad:").pack(anchor="w", pady=(10, 5))
        self.entry_edad = ctk.CTkEntry(frame, width=300)
        self.entry_edad.pack()
        
        ctk.CTkLabel(frame, text="Curso:").pack(anchor="w", pady=(10, 5))
        self.entry_curso = ctk.CTkEntry(frame, width=300)
        self.entry_curso.pack()
        
        if self.estudiante:
            self.entry_nombre.insert(0, self.estudiante["nombre"])
            self.entry_edad.insert(0, str(self.estudiante["edad"]))
            self.entry_curso.insert(0, self.estudiante["curso"])
            
        frame_botones = ctk.CTkFrame(frame)
        frame_botones.pack(pady=20)
        ctk.CTkButton(frame_botones, text="💾 Guardar", width=120, fg_color="#28A745", 
                     command=self.guardar).pack(side="left", padx=10)
        ctk.CTkButton(frame_botones, text="❌ Cancelar", width=120, fg_color="#6C757D", 
                     command=self.destroy).pack(side="left", padx=10)
        
    def guardar(self):
        nombre = self.entry_nombre.get().strip()
        edad_texto = self.entry_edad.get().strip()
        curso = self.entry_curso.get().strip()
        
        if not all([nombre, edad_texto, curso]):
            messagebox.showerror("Error", "❌ Todos los campos son obligatorios")
            return
        try:
            edad = int(edad_texto)
            if edad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "❌ Edad inválida")
            return
            
        datos = {"nombre": nombre, "edad": edad, "curso": curso}
        if self.estudiante:
            datos["id"] = self.estudiante["id"]
        self.callback(datos)
        self.destroy()