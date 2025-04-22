import tkinter as tk
from tkinter import messagebox
import requests

class VentanaCrearLicencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Crear Licencia Comercial")
        self.geometry("400x350")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        tk.Label(self, text="Crear Licencia Comercial", font=("Arial", 16, "bold")).pack(pady=15)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        campos = [
            ("Código de Licencia:", "codigo"),
            ("Representante Legal:", "representanteLegal"),
            ("Fecha de Vencimiento (YYYY-MM-DD):", "fechaVencimiento"),
            ("ID del Predio:", "idPredio"),
        ]

        self.entries = {}

        for i, (label_text, key) in enumerate(campos):
            tk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(form_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[key] = entry

        tk.Button(self, text="Crear Licencia", command=self.crear_licencia).pack(pady=15)

    def crear_licencia(self):
        codigo = self.entries["codigo"].get().strip()
        representante = self.entries["representanteLegal"].get().strip()
        fecha = self.entries["fechaVencimiento"].get().strip()
        id_predio = self.entries["idPredio"].get().strip()

        if not codigo or not representante or not fecha or not id_predio:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if not id_predio.isdigit():
            messagebox.showerror("Error", "El ID del predio debe ser un número.")
            return

        data = {
            "codigo": codigo,
            "representanteLegal": representante,
            "fechaVencimiento": fecha,
            "idPredio": int(id_predio)
        }

        try:
            response = requests.post("http://localhost:8081/licencia/crear", json=data)

            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Licencia creada exitosamente.")
                self.destroy()
            else:
                messagebox.showerror("Error", f"Error del servidor: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar con el servidor: {str(e)}")

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
