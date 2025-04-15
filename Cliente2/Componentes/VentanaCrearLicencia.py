import tkinter as tk
from tkinter import ttk

class VentanaCrearLicencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Crear Licencia Comercial")
        self.geometry("400x400")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        # Título centrado
        titulo = tk.Label(self, text="Crear Licencia Comercial", font=("Arial", 16))
        titulo.pack(pady=20)

        # Contenedor para los campos
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        # Campo 1
        tk.Label(form_frame, text="Número de Licencia:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry1 = tk.Entry(form_frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        # Campo 2
        tk.Label(form_frame, text="Fecha de Expedición:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry2 = tk.Entry(form_frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        # Campo 3
        tk.Label(form_frame, text="Fecha de Vencimiento:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry3 = tk.Entry(form_frame)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)

        # Campo 4
        tk.Label(form_frame, text="Estado:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry4 = tk.Entry(form_frame)
        self.entry4.grid(row=3, column=1, padx=5, pady=5)

        # Botón centrado
        crear_btn = tk.Button(self, text="Crear Licencia Comercial", command=self.crear_licencia)
        crear_btn.pack(pady=20)

    def crear_licencia(self):
        # Aquí puedes manejar la lógica de creación
        print("Licencia creada con los siguientes datos:")
        print("Campo 1:", self.entry1.get())
        print("Campo 2:", self.entry2.get())
        print("Campo 3:", self.entry3.get())
        print("Campo 4:", self.entry4.get())

    def centrar_ventana(self):
        self.update_idletasks()  # Asegura que la ventana se haya creado completamente

        ancho = self.winfo_width()
        alto = self.winfo_height()
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    
