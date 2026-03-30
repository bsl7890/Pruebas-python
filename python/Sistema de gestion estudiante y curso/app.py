import sys
import os
import customtkinter as ctk

# Agregar el directorio actual al PATH para imports correctos
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from interfaz.ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    # Configuración global de apariencia
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Crear y ejecutar la aplicación
    app = VentanaPrincipal()
    app.mainloop()