import tkinter as tk
from tkinter import messagebox
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
        tk.Label(self, text="Crear Predio Comercial", font=("Arial", 16, "bold")).pack(pady=15)

        # Contenedor para el formulario
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        # Campos
        labels = [
            "Propietario:", "Dirección:", "Estrato (1-6):",
            "Consumo m³:", "Tipo Comercio:", "Fecha de Registro:"
        ]

        self.entries = []
        for i, label_text in enumerate(labels):
            tk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        # Valor por defecto para fecha
        self.entries[-1].insert(0, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

        # Botón de creación
        tk.Button(self, text="Crear Predio Comercial", command=self.crear_comercial).pack(pady=20)

    def crear_comercial(self):
        try:
            # Validar campos
            for entry in self.entries[:-1]:  # Excluir fecha
                if not entry.get().strip():
                    messagebox.showerror("Error", "Todos los campos son obligatorios (excepto fecha).")
                    return

            try:
                estrato = int(self.entries[2].get().strip())
                consumo = float(self.entries[3].get().strip())
                if not (1 <= estrato <= 6):
                    messagebox.showerror("Error", "Estrato debe estar entre 1 y 6.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Estrato debe ser entero y Consumo debe ser numérico.")
                return

            data = {
                "propietario": self.entries[0].get().strip(),
                "direccion": self.entries[1].get().strip(),
                "estrato": estrato,
                "consumo": consumo,
                "tipoComercio": self.entries[4].get().strip(),
                "fechaRegistro": self.entries[5].get().strip()
            }

            response = requests.post(
                url="http://localhost:8081/predio/crear",
                headers={"Content-Type": "application/json"},
                data=json.dumps(data)
            )

            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Predio creado correctamente.")
                self.destroy()
            else:
                messagebox.showerror("Error", f"Error al crear predio: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")