# test_import.py
import os
import sys

print("=" * 50)
print("🔍 DIAGNÓSTICO DE IMPORTACIÓN")
print("=" * 50)

# 1. Directorio actual
print(f"\n📁 Directorio de trabajo: {os.getcwd()}")

# 2. Directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"📁 Directorio del script: {script_dir}")

# 3. Contenido del directorio
print(f"\n📂 Archivos en el directorio:")
for archivo in os.listdir():
    print(f"   - {archivo}")

# 4. Contenido de la carpeta interfaz
print(f"\n📂 Archivos en interfaz/:")
if os.path.exists("interfaz"):
    for archivo in os.listdir("interfaz"):
        print(f"   - {archivo}")
else:
    print("   ❌ La carpeta 'interfaz' NO existe")

# 5. Verificar sys.path
print(f"\n🔍 sys.path:")
for ruta in sys.path[:5]:  # Mostrar las primeras 5 rutas
    print(f"   - {ruta}")

# 6. Intentar importación
print(f"\n🔄 Intentando importar...")
try:
    sys.path.insert(0, script_dir)
    from interfaz.ventana_principal import VentanaPrincipal
    print("✅ ¡IMPORTACIÓN EXITOSA!")
except Exception as e:
    print(f"❌ ERROR: {type(e).__name__}: {e}")

print("=" * 50)