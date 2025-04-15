import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import requests
import json

class VentanaCrearComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Crear Predio Comercial")
        self.geometry("450x400")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        # Título
        titulo = tk.Label(self, text="Crear Predio Comercial", font=("Arial", 16, "bold"))
        titulo.pack(pady=15)

        # Contenedor para el formulario
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        # Campos
        labels = [
            "Propietario:", "Dirección:", "Estado de Cuenta (AC/INAC):", 
            "Estrato (1-6):", "Consumo m3:", "Subsidio:", 
            "Tipo de Vivienda:", "Fecha de Registro:"
        ]

        self.entries = []

        for i, label_text in enumerate(labels):
            tk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, padx=1, pady=5)
            self.entries.append(entry)

        # Valor por defecto para fecha
        self.entries[-1].insert(0, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

        # Botón de creación
        btn_crear = tk.Button(self, text="Crear Predio Comercial", command=self.crear_comercial)
        btn_crear.pack(pady=20)

    def crear_comercial(self):
        try:
            data = {
                "propietario": self.entries[0].get().strip(),
                "direccion": self.entries[1].get().strip(),
                "estadoCuenta": self.entries[2].get().strip(),
                "estrato": int(self.entries[3].get().strip()),
                "consumo": float(self.entries[4].get().strip()),
                "subsidio": int(self.entries[5].get().strip()),
                "tipoVivienda": self.entries[6].get().strip(),
                "fechaRegistro": self.entries[7].get().strip(),
            }

            response = requests.post(
                url="http://localhost:8081/predio/crear",
                headers={"Content-Type": "application/json"},
                data=json.dumps(data)
            )

            messagebox.showinfo("Resultado", f"Código de respuesta: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")
