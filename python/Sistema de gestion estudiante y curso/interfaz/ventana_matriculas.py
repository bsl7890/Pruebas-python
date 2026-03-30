import customtkinter as ctk
from tkinter import messagebox, ttk
import json
import os

class VentanaMatriculas(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.padre = padre
        
        self.title("📝 Gestión de Matrículas")
        self.geometry("900x650")
        self.resizable(False, False)
        
        self.directorio = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.archivo_matriculas = os.path.join(self.directorio, "datos_matriculas.json")
        self.archivo_estudiantes = os.path.join(self.directorio, "datos_estudiantes.json")
        self.archivo_cursos = os.path.join(self.directorio, "datos_cursos.json")
        
        self.matriculas = self.cargar_datos(self.archivo_matriculas)
        self.estudiantes = self.cargar_datos(self.archivo_estudiantes)
        self.cursos = self.cargar_datos(self.archivo_cursos)
        
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.crear_interfaz()
        
    def cargar_datos(self, archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
            
    def guardar_datos(self):
        with open(self.archivo_matriculas, "w", encoding="utf-8") as f:
            json.dump(self.matriculas, f, indent=2, ensure_ascii=False)
            
    def cerrar_ventana(self):
        self.destroy()
            
    def crear_interfaz(self):
        frame_superior = ctk.CTkFrame(self)
        frame_superior.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(frame_superior, text="📝 Gestión de Matrículas", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=10)
        ctk.CTkButton(frame_superior, text="⬅ Volver", width=100, 
                     command=self.cerrar_ventana).pack(side="right", padx=10)
        
        frame_controles = ctk.CTkFrame(self)
        frame_controles.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkButton(frame_controles, text="➕ Matricular", width=120, fg_color="#2E86AB",
                     command=self.abrir_formulario_matricula).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="🗑️ Eliminar", width=120, fg_color="#C73E1D",
                     command=self.eliminar_matricula).pack(side="left", padx=5)
        ctk.CTkButton(frame_controles, text="🔄 Refrescar", width=120,
                     command=self.refrescar_tabla).pack(side="left", padx=5)
        
        ctk.CTkLabel(frame_controles, text="🔍 Buscar:").pack(side="left", padx=(20, 5))
        self.entry_buscar = ctk.CTkEntry(frame_controles, width=200, placeholder_text="Estudiante")
        self.entry_buscar.pack(side="left", padx=5)
        self.entry_buscar.bind("<KeyRelease>", lambda e: self.buscar_matricula())
        
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
        
        style = ttk.Style()
        style.theme_use("clam")
        columns = ("id", "estudiante", "curso", "fecha")
        self.tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings", height=15)
        
        for col, text in zip(columns, ["ID", "Estudiante", "Curso", "Fecha"]):
            self.tabla.heading(col, text=text)
        self.tabla.column("id", width=80, anchor="center")
        self.tabla.column("estudiante", width=300, anchor="w")
        self.tabla.column("curso", width=300, anchor="w")
        self.tabla.column("fecha", width=150, anchor="center")
        
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
        for mat in self.matriculas:
            self.tabla.insert("", "end", values=(mat.get("id"), mat.get("nombre_estudiante"), 
                                                  mat.get("nombre_curso"), mat.get("fecha")))
        self.label_total.configure(text=f"📊 Total: {len(self.matriculas)} matrícula(s)")
        
    def abrir_formulario_matricula(self):
        if not self.estudiantes or not self.cursos:
            messagebox.showwarning("Advertencia", "⚠️ Debe haber estudiantes y cursos registrados")
            return
        FormularioMatricula(self, self.agregar_matricula, self.estudiantes, self.cursos)
        
    def agregar_matricula(self, datos):
        # Verificar duplicado
        for mat in self.matriculas:
            if mat["id_estudiante"] == datos["id_estudiante"] and mat["id_curso"] == datos["id_curso"]:
                messagebox.showerror("Error", "❌ Ya está matriculado en este curso")
                return
        nuevo_id = max([m.get("id", 0) for m in self.matriculas], default=0) + 1
        self.matriculas.append({"id": nuevo_id, **datos})
        self.guardar_datos()
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", "✅ Matrícula registrada")
        
    def eliminar_matricula(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "⚠️ Selecciona una matrícula")
            return
        id_eliminar = self.tabla.item(seleccion[0])["values"][0]
        if messagebox.askyesno("Confirmar", "¿Eliminar esta matrícula?"):
            self.matriculas = [m for m in self.matriculas if m["id"] != id_eliminar]
            self.guardar_datos()
            self.refrescar_tabla()
            messagebox.showinfo("Éxito", "🗑️ Matrícula eliminada")
            
    def buscar_matricula(self):
        texto = self.entry_buscar.get().lower()
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for mat in self.matriculas:
            if texto in mat.get("nombre_estudiante", "").lower():
                self.tabla.insert("", "end", values=(mat["id"], mat["nombre_estudiante"], 
                                                      mat["nombre_curso"], mat.get("fecha")))


class FormularioMatricula(ctk.CTkToplevel):
    def __init__(self, padre, callback, estudiantes, cursos):
        super().__init__(padre)
        self.callback = callback
        self.estudiantes = estudiantes
        self.cursos = cursos
        self.title("📝 Matricular Estudiante")
        self.geometry("450x400")
        self.resizable(False, False)
        self.transient(padre)
        self.grab_set()
        self.crear_formulario()
        
    def crear_formulario(self):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Estudiante:").pack(anchor="w", pady=(10, 5))
        self.combo_estudiantes = ctk.CTkComboBox(frame, width=300, 
            values=[f"{e['id']} - {e['nombre']}" for e in self.estudiantes])
        self.combo_estudiantes.pack()
        
        ctk.CTkLabel(frame, text="Curso:").pack(anchor="w", pady=(10, 5))
        self.combo_cursos = ctk.CTkComboBox(frame, width=300,
            values=[f"{c['id']} - {c['asignatura']}" for c in self.cursos])
        self.combo_cursos.pack()
        
        ctk.CTkLabel(frame, text="Fecha (DD/MM/AAAA):").pack(anchor="w", pady=(10, 5))
        self.entry_fecha = ctk.CTkEntry(frame, width=300)
        self.entry_fecha.pack()
        
        frame_botones = ctk.CTkFrame(frame)
        frame_botones.pack(pady=20)
        ctk.CTkButton(frame_botones, text="💾 Guardar", width=120, fg_color="#28A745", 
                     command=self.guardar).pack(side="left", padx=10)
        ctk.CTkButton(frame_botones, text="❌ Cancelar", width=120, fg_color="#6C757D", 
                     command=self.destroy).pack(side="left", padx=10)
        
    def guardar(self):
        est_sel = self.combo_estudiantes.get()
        cur_sel = self.combo_cursos.get()
        fecha = self.entry_fecha.get().strip()
        
        if not all([est_sel, cur_sel, fecha]):
            messagebox.showerror("Error", "❌ Completa todos los campos")
            return
            
        id_est = int(est_sel.split(" - ")[0])
        id_cur = int(cur_sel.split(" - ")[0])
        est = next((e for e in self.estudiantes if e["id"] == id_est), None)
        cur = next((c for c in self.cursos if c["id"] == id_cur), None)
        
        if est and cur:
            self.callback({
                "id_estudiante": id_est, "nombre_estudiante": est["nombre"],
                "id_curso": id_cur, "nombre_curso": cur["asignatura"], "fecha": fecha
            })
            self.destroy()