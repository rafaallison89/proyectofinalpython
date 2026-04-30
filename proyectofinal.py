import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\n proyecto Escolar\n Versión 1.0")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - rafellise")
ventana.geometry("500x600")
ventana.resizable(False, False)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------
# FONDO (WALLPAPER REAL)
# -------------------------
fondo_label = None

try:
    fondo_img = Image.open(os.path.join(BASE_DIR, "fondo.png"))
    fondo_img = fondo_img.resize((500, 600))
    fondo = ImageTk.PhotoImage(fondo_img)

    fondo_label = tk.Label(ventana, image=fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    print("No se encontró fondo.png")

# -------------------------
# LOGO
# -------------------------
try:
    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((200, 200))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo, bg="#000000", bd=0)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo)", font=("Arial", 14), bg="#000000", fg="white")
    lbl_sin_logo.pack(pady=40)

# -------------------------
# ESTILO BOTONES
# -------------------------
btn_config = {
    "bg": "black",
    "fg": "white",
    "font": ("Arial", 12, "italic"),
    "width": 25,
    "height": 2,
    "relief": "flat",
    "bd": 0,
    "activebackground": "#333333",
    "activeforeground": "white",
    "cursor": "hand2"
}

# -------------------------
# BOTONES
# -------------------------
btn_reg_prod = tk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos, **btn_config)
btn_reg_prod.pack(pady=8)

btn_reg_ventas = tk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas, **btn_config)
btn_reg_ventas.pack(pady=8)

btn_reportes = tk.Button(ventana, text="Reportes", command=abrir_reportes, **btn_config)
btn_reportes.pack(pady=8)

btn_acerca = tk.Button(ventana, text="Acerca de", command=abrir_acerca_de, **btn_config)
btn_acerca.pack(pady=8)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()