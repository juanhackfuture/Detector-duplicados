import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------------------------------------------------------
# LÓGICA: misma función de hash del código original
# ---------------------------------------------------------------
def obtener_hash(ruta_archivo):
    with open(ruta_archivo, "rb") as f:
        contenido = f.read()
        return hashlib.md5(contenido).hexdigest()

# ---------------------------------------------------------------
# ACCIÓN: seleccionar carpeta con el explorador de archivos
# ---------------------------------------------------------------
def seleccionar_carpeta():
    ruta = filedialog.askdirectory(title="Selecciona una carpeta")
    if ruta:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta)

# ---------------------------------------------------------------
# ACCIÓN PRINCIPAL: buscar duplicados y mostrarlos en pantalla
# ---------------------------------------------------------------
def buscar_duplicados():
    ruta = entrada_ruta.get().strip()

    # Validar ruta
    if not ruta or not os.path.exists(ruta):
        messagebox.showerror("Error", "Ruta no válida. Selecciona una carpeta existente.")
        return

    # Limpiar resultados anteriores
    cuadro_resultado.config(state=tk.NORMAL)
    cuadro_resultado.delete("1.0", tk.END)

    archivos = os.listdir(ruta)
    hashes = {}
    duplicados = []

    for archivo in archivos:
        ruta_completa = os.path.join(ruta, archivo)
        if os.path.isdir(ruta_completa):
            continue
        try:
            hash_archivo = obtener_hash(ruta_completa)
            if hash_archivo in hashes:
                duplicados.append((archivo, hashes[hash_archivo]))
            else:
                hashes[hash_archivo] = archivo
        except Exception:
            continue  # Si un archivo no se puede leer, lo salta

    # Mostrar resultados
    if not duplicados:
        cuadro_resultado.insert(tk.END, "✅ No se encontraron archivos duplicados.\n")
    else:
        cuadro_resultado.insert(tk.END, f"⚠️ Se encontraron {len(duplicados)} duplicado(s):\n\n")
        for dup, original in duplicados:
            cuadro_resultado.insert(tk.END, f"📄 '{dup}'\n    es duplicado de → '{original}'\n\n")

    cuadro_resultado.insert(tk.END, f"Total duplicados: {len(duplicados)}")
    cuadro_resultado.config(state=tk.DISABLED)

# ---------------------------------------------------------------
# INTERFAZ GRÁFICA
# ---------------------------------------------------------------
ventana = tk.Tk()
ventana.title("🔍 Detector de Archivos Duplicados")
ventana.geometry("620x460")
ventana.resizable(False, False)
ventana.configure(bg="#1e1e2e")

# --- Título ---
titulo = tk.Label(
    ventana,
    text="🔍 Detector de Archivos Duplicados",
    font=("Segoe UI", 16, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4"
)
titulo.pack(pady=(20, 4))

subtitulo = tk.Label(
    ventana,
    text="Encuentra archivos con contenido idéntico en una carpeta",
    font=("Segoe UI", 9),
    bg="#1e1e2e",
    fg="#6c7086"
)
subtitulo.pack(pady=(0, 20))

# --- Fila: entrada de ruta + botón explorar ---
frame_ruta = tk.Frame(ventana, bg="#1e1e2e")
frame_ruta.pack(padx=30, fill="x")

entrada_ruta = tk.Entry(
    frame_ruta,
    font=("Segoe UI", 10),
    bg="#313244",
    fg="#cdd6f4",
    insertbackground="#cdd6f4",
    relief="flat",
    bd=8
)
entrada_ruta.pack(side="left", fill="x", expand=True, ipady=6)

boton_explorar = tk.Button(
    frame_ruta,
    text="📁 Explorar",
    font=("Segoe UI", 10),
    bg="#89b4fa",
    fg="#1e1e2e",
    activebackground="#74c7ec",
    relief="flat",
    cursor="hand2",
    padx=12,
    command=seleccionar_carpeta
)
boton_explorar.pack(side="left", padx=(8, 0), ipady=6)

# --- Botón buscar ---
boton_buscar = tk.Button(
    ventana,
    text="🔍 Buscar Duplicados",
    font=("Segoe UI", 11, "bold"),
    bg="#a6e3a1",
    fg="#1e1e2e",
    activebackground="#94e2d5",
    relief="flat",
    cursor="hand2",
    padx=20,
    command=buscar_duplicados
)
boton_buscar.pack(pady=16, ipady=8)

# --- Área de resultados ---
frame_resultado = tk.Frame(ventana, bg="#1e1e2e")
frame_resultado.pack(padx=30, fill="both", expand=True)

label_resultado = tk.Label(
    frame_resultado,
    text="Resultados:",
    font=("Segoe UI", 10, "bold"),
    bg="#1e1e2e",
    fg="#cdd6f4",
    anchor="w"
)
label_resultado.pack(fill="x", pady=(0, 4))

cuadro_resultado = tk.Text(
    frame_resultado,
    font=("Segoe UI", 10),
    bg="#313244",
    fg="#cdd6f4",
    relief="flat",
    bd=8,
    state=tk.DISABLED,
    wrap="word",
    height=12
)
cuadro_resultado.pack(fill="both", expand=True)

# --- Footer ---
footer = tk.Label(
    ventana,
    text="Desarrollado con Python + tkinter",
    font=("Segoe UI", 8),
    bg="#1e1e2e",
    fg="#45475a"
)
footer.pack(pady=10)

ventana.mainloop()