import customtkinter as ctk
from tkinter import messagebox, ttk
import json
import os

# ✅ Lista de 42 asignaturas predefinidas
ASIGNATURAS_PREDEFINIDAS = [
    "Programación", "Diseño de software", "Desarrollo web",
    "Desarrollo de aplicaciones móviles", "Desarrollo de videojuegos", 
    "Inteligencia artificial", "Ciencia de datos", "Big data", 
    "Ciberseguridad", "Matemáticas", "Física", "Química",
    "Biología", "Historia", "Geografía", "Filosofía", 
    "Psicología", "Sociología", "Economía", "Política", 
    "Derecho", "Antropología", "Arqueología", "Lingüística", 
    "Literatura", "Arte", "Música", "Danza", 
    "Teatro", "Cine", "Fotografía", "Escultura", 
    "Pintura", "Dibujo", "Emprendimiento", "Marketing", 
    "Ventas", "Finanzas", "Contabilidad", "Recursos humanos", 
    "Administración", "Logística"
]

class VentanaCursos(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.padre = padre
        
        self.title("📚 Gestión de Cursos")
        self.geometry("900x650")
        self.resizable(False, False)
        
        self.directorio = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.archivo_datos = os.path.join(self.directorio, "datos_cursos.json")
        self.cursos = self.cargar_datos()
        
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.crear_interfaz()
        
    def cargar_datos(self):
        try:
            with open(self.archivo_datos, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
            
    def guardar_datos(self):
        with open(self.archivo_datos, "w", encoding="utf-8") as f:
            json.dump(self.cursos, f, indent=2, ensure_ascii=False)
            
    def cerrar_ventana(self):
        self.destroy()
            
    def crear_interfaz(self):
        frame_superior = ctk.CTkFrame(self)
        frame_superior.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(frame_superior, text="📚 Gestión de Cursos", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=10)
        ctk.CTkButton(frame_superior, text="⬅ Volver", width=100, 
                     command=self.cerrar_ventana).pack(side="right", padx=10)
        
        frame_controles = ctk.CTkFrame(self)
        frame_controles.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkButton(frame_controles, text="➕ Agregar", width=120, fg_color="#A23B72",
                     command=self.abrir_formulario_agregar).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="✏️ Editar", width=120, fg_color="#F18F01",
                     command=self.editar_curso).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="🗑️ Eliminar", width=120, fg_color="#C73E1D",
                     command=self.eliminar_curso).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="🔄 Refrescar", width=120,
                     command=self.refrescar_tabla).pack(side="left", padx=5)
        
        ctk.CTkLabel(frame_controles, text="🔍 Buscar:").pack(side="left", padx=(20, 5))
        self.entry_buscar = ctk.CTkEntry(frame_controles, width=200, placeholder_text="Curso")
        self.entry_buscar.pack(side="left", padx=5)
        self.entry_buscar.bind("<KeyRelease>", lambda e: self.buscar_curso())
        
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
        
        style = ttk.Style()
        style.theme_use("clam")
        columns = ("id", "asignatura", "horario", "docente")
        self.tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings", height=15)
        
        for col, text in zip(columns, ["ID", "Asignatura", "Horario", "Docente"]):
            self.tabla.heading(col, text=text)
        self.tabla.column("id", width=80, anchor="center")
        self.tabla.column("asignatura", width=350, anchor="w")
        self.tabla.column("horario", width=150, anchor="center")
        self.tabla.column("docente", width=200, anchor="w")
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.label_total = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.label_total.pack(pady=10)
        self.refrescar_tabla()
        
    def refrescar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for cur in self.cursos:
            self.tabla.insert("", "end", values=(cur.get("id"), cur.get("asignatura"), 
                                                  cur.get("horario"), cur.get("docente")))
        self.label_total.configure(text=f"📊 Total: {len(self.cursos)} curso(s)")
        
    def abrir_formulario_agregar(self):
        FormularioCurso(self, self.agregar_curso)
        
    def agregar_curso(self, datos):
        nuevo_id = max([c.get("id", 0) for c in self.cursos], default=0) + 1
        self.cursos.append({"id": nuevo_id, **datos})
        self.guardar_datos()
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", "✅ Curso agregado")
        
    def editar_curso(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "⚠️ Selecciona un curso")
            return
        curso = next((c for c in self.cursos if c["id"] == self.tabla.item(seleccion[0])["values"][0]), None)
        if curso:
            FormularioCurso(self, self.actualizar_curso, curso)
        
    def actualizar_curso(self, datos):
        for i, cur in enumerate(self.cursos):
            if cur["id"] == datos["id"]:
                self.cursos[i] = datos
                break
        self.guardar_datos()
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", "✅ Curso actualizado")
        
    def eliminar_curso(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "⚠️ Selecciona un curso")
            return
        id_eliminar = self.tabla.item(seleccion[0])["values"][0]
        if messagebox.askyesno("Confirmar", f"¿Eliminar curso ID {id_eliminar}?"):
            self.cursos = [c for c in self.cursos if c["id"] != id_eliminar]
            self.guardar_datos()
            self.refrescar_tabla()
            messagebox.showinfo("Éxito", "🗑️ Curso eliminado")
            
    def buscar_curso(self):
        texto = self.entry_buscar.get().lower()
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for cur in self.cursos:
            if texto in cur.get("asignatura", "").lower():
                self.tabla.insert("", "end", values=(cur["id"], cur["asignatura"], 
                                                      cur.get("horario"), cur.get("docente")))


class FormularioCurso(ctk.CTkToplevel):
    """Formulario con ComboBox para Asignatura (42 opciones) y Horario (2 opciones)"""
    
    def __init__(self, padre, callback, curso=None):
        super().__init__(padre)
        self.callback = callback
        self.curso = curso
        self.title("✏️ Agregar Curso" if not curso else "✏️ Editar Curso")
        self.geometry("450x450")  # ⭐ Un poco más alto para el combo largo
        self.resizable(False, False)
        self.transient(padre)
        self.grab_set()
        self.crear_formulario()
        
    def crear_formulario(self):
        """Crea el formulario con ComboBox para Asignatura y Horario"""
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # ⭐ ASIGNATURA - ComboBox con 42 opciones predefinidas
        ctk.CTkLabel(frame, text="Asignatura:").pack(anchor="w", pady=(10, 5))
        self.combo_asignatura = ctk.CTkComboBox(
            frame, 
            width=350, 
            values=ASIGNATURAS_PREDEFINIDAS,
            state="readonly"  # ✅ Solo selección, no escritura manual
        )
        self.combo_asignatura.pack()
        self.combo_asignatura.set("Programación")  # Valor por defecto
        
        # ⭐ HORARIO - ComboBox con 2 opciones
        ctk.CTkLabel(frame, text="Horario:").pack(anchor="w", pady=(10, 5))
        self.combo_horario = ctk.CTkComboBox(
            frame, 
            width=350, 
            values=["Diurno", "Vespertino"],
            state="readonly"
        )
        self.combo_horario.pack()
        self.combo_horario.set("Diurno")  # Valor por defecto
        
        # DOCENTE - Entry normal (texto libre)
        ctk.CTkLabel(frame, text="Docente:").pack(anchor="w", pady=(10, 5))
        self.entry_docente = ctk.CTkEntry(frame, width=350)
        self.entry_docente.pack()
        
        # ⭐ Cargar datos si es edición
        if self.curso:
            # Configurar combo de asignatura con valor existente
            asignatura_guardada = self.curso.get("asignatura", "Programación")
            if asignatura_guardada in ASIGNATURAS_PREDEFINIDAS:
                self.combo_asignatura.set(asignatura_guardada)
            else:
                self.combo_asignatura.set("Programación")  # Por defecto si no coincide
            
            # Configurar combo de horario
            horario_guardado = self.curso.get("horario", "Diurno")
            if horario_guardado in ["Diurno", "Vespertino"]:
                self.combo_horario.set(horario_guardado)
            else:
                self.combo_horario.set("Diurno")
            
            # Cargar docente
            self.entry_docente.insert(0, self.curso.get("docente", ""))
                
        # Botones
        frame_botones = ctk.CTkFrame(frame)
        frame_botones.pack(pady=20)
        ctk.CTkButton(frame_botones, text="💾 Guardar", width=120, fg_color="#28A745", 
                     command=self.guardar).pack(side="left", padx=10)
        ctk.CTkButton(frame_botones, text="❌ Cancelar", width=120, fg_color="#6C757D", 
                     command=self.destroy).pack(side="left", padx=10)
        
    def guardar(self):
        """Guarda y valida los datos"""
        asignatura = self.combo_asignatura.get()  # ✅ Del ComboBox
        horario = self.combo_horario.get()        # ✅ Del ComboBox
        docente = self.entry_docente.get().strip()  # Del Entry
        
        # Validaciones
        if not asignatura:
            messagebox.showerror("Error", "❌ La asignatura es obligatoria")
            return
        if not docente:
            messagebox.showerror("Error", "❌ El docente es obligatorio")
            return
            
        # Preparar datos
        datos = {
            "asignatura": asignatura,      # ✅ Garantizado: una de las 42 opciones
            "horario": horario,            # ✅ Garantizado: Diurno o Vespertino
            "docente": docente
        }
        
        if self.curso:  # Si es edición, mantener el ID
            datos["id"] = self.curso["id"]
            
        self.callback(datos)
        self.destroy()