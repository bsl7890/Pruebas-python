import customtkinter as ctk
from tkinter import messagebox
from .ventana_estudiantes import VentanaEstudiantes
from .ventana_cursos import VentanaCursos
from .ventana_matriculas import VentanaMatriculas

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("🎓 Sistema de Gestión Escolar")
        self.geometry("600x500")
        self.resizable(False, False)
        self.center_window()
        
        # Crear interfaz
        self.crear_interfaz()
        
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz principal"""
        
        frame_principal = ctk.CTkFrame(self)
        frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        label_titulo = ctk.CTkLabel(
            frame_principal, 
            text="🎓 Sistema de Gestión Escolar", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        label_titulo.pack(pady=(30, 10))
        
        label_subtitulo = ctk.CTkLabel(
            frame_principal, 
            text="Administra estudiantes, cursos y matrículas", 
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        label_subtitulo.pack(pady=(0, 30))
        
        # Botones del menú
        self.crear_boton(frame_principal, "🎓 Gestionar Estudiantes", self.abrir_estudiantes, "#2E86AB")
        self.crear_boton(frame_principal, "📚 Gestionar Cursos", self.abrir_cursos, "#A23B72")
        self.crear_boton(frame_principal, "📝 Gestionar Matrículas", self.abrir_matriculas, "#F18F01")
        
        # Botón de salir
        btn_salir = ctk.CTkButton(
            frame_principal,
            text="🚪 Salir del Sistema",
            width=300,
            height=45,
            font=ctk.CTkFont(size=16),
            fg_color="#C73E1D",
            hover_color="#A33216",
            command=self.confirmar_salida
        )
        btn_salir.pack(pady=20)
        
    def crear_boton(self, padre, texto, comando, color):
        """Crea un botón estilizado"""
        btn = ctk.CTkButton(
            padre,
            text=texto,
            width=300,
            height=45,
            font=ctk.CTkFont(size=16),
            fg_color=color,
            hover_color=color,
            command=comando
        )
        btn.pack(pady=10)
        
    def abrir_estudiantes(self):
        """Abre la ventana de estudiantes como modal"""
        ventana = VentanaEstudiantes(self)
        ventana.transient(self)
        ventana.grab_set()
        
    def abrir_cursos(self):
        """Abre la ventana de cursos como modal"""
        ventana = VentanaCursos(self)
        ventana.transient(self)
        ventana.grab_set()
        
    def abrir_matriculas(self):
        """Abre la ventana de matrículas como modal"""
        ventana = VentanaMatriculas(self)
        ventana.transient(self)
        ventana.grab_set()
        
    def confirmar_salida(self):
        """Confirma antes de salir del sistema"""
        if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir del sistema?"):
            self.destroy()