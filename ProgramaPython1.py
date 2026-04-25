# programa en python en repositorios

import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("600x400")  # Aumenté el tamaño de la ventana

# Configurar fondo negro de la ventana
ventana.configure(bg="black")

# Crear la etiqueta con texto, fuente elegante/cursiva, tamaño grande y color llamativo
etiqueta = tk.Label(ventana,
                    text="Este programa es de Allison y Rafa",
                    font=("Times New Roman", 24, "italic"),  # Fuente elegante en cursiva
                    fg="cyan",  # Color del texto (cian)
                    bg="black",  # Fondo negro
                    padx=20,  # Espaciado alrededor del texto
                    pady=20)  # Espaciado alrededor del texto

# Centrar la etiqueta en la ventana
etiqueta.pack(expand=True)

# Iniciar la interfaz gráfica
ventana.mainloop()