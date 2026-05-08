import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COLOR_FONDO = "#111111"
COLOR_PANEL = "#1b1b1b"
COLOR_INPUT = "#262626"
COLOR_BOTON = "#d4af37"
COLOR_TEXTO = "#ffffff"
COLOR_SECUNDARIO = "#b0b0b0"

FUENTE_TITULO = ("Segoe UI", 20, "bold")
FUENTE_LABEL = ("Segoe UI", 11)
FUENTE_INPUT = ("Segoe UI", 11)
FUENTE_BOTON = ("Segoe UI", 11, "bold")

# =====================================================
# FUNCIONES
# =====================================================

def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x650")
    reg.configure(bg=COLOR_FONDO)
    reg.resizable(False, False)

    # -------------------------------------------------
    # PANEL CENTRAL
    # -------------------------------------------------

    panel = tk.Frame(
        reg,
        bg=COLOR_PANEL,
        width=420,
        height=560
    )

    panel.place(relx=0.5, rely=0.5, anchor="center")

    # -------------------------------------------------
    # LOGO
    # -------------------------------------------------

    try:
        logo_path = os.path.join(BASE_DIR, "logo.png")

        logo = Image.open(logo_path)
        logo = logo.resize((110, 110))

        logo_img = ImageTk.PhotoImage(logo)

        lbl_logo = tk.Label(
            panel,
            image=logo_img,
            bg=COLOR_PANEL
        )

        lbl_logo.image = logo_img
        lbl_logo.pack(pady=(25, 10))

    except:
        pass

    # -------------------------------------------------
    # TITULO
    # -------------------------------------------------

    titulo = tk.Label(
        panel,
        text="Registro de Productos",
        font=FUENTE_TITULO,
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO
    )

    titulo.pack(pady=(5, 25))

    # -------------------------------------------------
    # FUNCIÓN PARA CREAR CAMPOS
    # -------------------------------------------------

    def crear_campo(texto):

        lbl = tk.Label(
            panel,
            text=texto,
            font=FUENTE_LABEL,
            bg=COLOR_PANEL,
            fg=COLOR_SECUNDARIO
        )

        lbl.pack(anchor="w", padx=40, pady=(8, 4))

        entry = tk.Entry(
            panel,
            font=FUENTE_INPUT,
            bg=COLOR_INPUT,
            fg=COLOR_TEXTO,
            insertbackground="white",
            relief="flat",
            width=30
        )

        entry.pack(ipady=10)

        return entry

    # -------------------------------------------------
    # CAMPOS
    # -------------------------------------------------

    txt_id = crear_campo("ID del Producto")
    txt_desc = crear_campo("Descripción")
    txt_precio = crear_campo("Precio")
    txt_categoria = crear_campo("Categoría")

    # -------------------------------------------------
    # GUARDAR PRODUCTO
    # -------------------------------------------------

    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # VALIDAR CAMPOS

        if not id_prod or not descripcion or not precio or not categoria:

            messagebox.showwarning(
                "Campos Vacíos",
                "Completa todos los campos."
            )

            return

        # VALIDAR PRECIO

        try:
            float(precio)

        except:

            messagebox.showerror(
                "Error",
                "El precio debe ser numérico."
            )

            return

        # GUARDAR ARCHIVO

        archivo_productos = os.path.join(BASE_DIR, "productos.txt")

        try:

            with open(archivo_productos, "a", encoding="utf-8") as archivo:

                archivo.write(
                    f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
                )

            messagebox.showinfo(
                "Guardado",
                "Producto registrado correctamente."
            )

            # LIMPIAR

            txt_id.delete(0, tk.END)
            txt_desc.delete(0, tk.END)
            txt_precio.delete(0, tk.END)
            txt_categoria.delete(0, tk.END)

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"No se pudo guardar:\n{e}"
            )

    # -------------------------------------------------
    # BOTÓN
    # -------------------------------------------------

    btn_guardar = tk.Button(
        panel,
        text="GUARDAR PRODUCTO",
        command=guardar_producto,
        bg=COLOR_BOTON,
        fg="black",
        font=FUENTE_BOTON,
        relief="flat",
        cursor="hand2",
        activebackground="#e5c158",
        width=24,
        height=2
    )

    btn_guardar.pack(pady=35)

# =====================================================
# MÓDULOS EXTRA
# =====================================================

def abrir_registro_ventas():

    messagebox.showinfo(
        "Ventas",
        "Módulo de ventas próximamente."
    )

def abrir_reportes():

    messagebox.showinfo(
        "Reportes",
        "Módulo de reportes próximamente."
    )

def abrir_acerca_de():

    messagebox.showinfo(
        "Acerca de",
        "Sistema Punto de Venta\nrafellise\nVersión 1.0"
    )

# =====================================================
# VENTANA PRINCIPAL
# =====================================================

ventana = tk.Tk()

ventana.title("Punto de Venta - rafellise")
ventana.geometry("550x700")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(False, False)

# =====================================================
# LOGO PRINCIPAL
# =====================================================

try:

    logo_path = os.path.join(BASE_DIR, "logo.png")

    logo = Image.open(logo_path)
    logo = logo.resize((180, 180))

    logo_main = ImageTk.PhotoImage(logo)

    lbl_logo = tk.Label(
        ventana,
        image=logo_main,
        bg=COLOR_FONDO
    )

    lbl_logo.pack(pady=(40, 15))

except:

    texto_logo = tk.Label(
        ventana,
        text="RAFELLISE",
        font=("Segoe UI", 26, "bold"),
        fg="white",
        bg=COLOR_FONDO
    )

    texto_logo.pack(pady=(50, 20))

# =====================================================
# TITULO
# =====================================================

titulo = tk.Label(
    ventana,
    text="Sistema Punto de Venta",
    font=("Segoe UI", 18, "bold"),
    bg=COLOR_FONDO,
    fg="white"
)

titulo.pack(pady=(0, 35))

# =====================================================
# ESTILO BOTONES
# =====================================================

btn_config = {
    "font": ("Segoe UI", 12, "bold"),
    "bg": COLOR_PANEL,
    "fg": "white",
    "activebackground": COLOR_BOTON,
    "activeforeground": "black",
    "relief": "flat",
    "bd": 0,
    "cursor": "hand2",
    "width": 24,
    "height": 2
}

# =====================================================
# BOTONES
# =====================================================

btn_reg_prod = tk.Button(
    ventana,
    text="Registro de Productos",
    command=abrir_registro_productos,
    **btn_config
)

btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(
    ventana,
    text="Registro de Ventas",
    command=abrir_registro_ventas,
    **btn_config
)

btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(
    ventana,
    text="Reportes",
    command=abrir_reportes,
    **btn_config
)

btn_reportes.pack(pady=10)

btn_acerca = tk.Button(
    ventana,
    text="Acerca de",
    command=abrir_acerca_de,
    **btn_config
)

btn_acerca.pack(pady=10)

# =====================================================
# INICIAR
# =====================================================

ventana.mainloop()
