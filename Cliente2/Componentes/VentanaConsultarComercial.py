import tkinter as tk
from tkinter import messagebox
import requests

class VentanaConsultarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Consultar Predio Comercial")
        self.geometry("500x400")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        tk.Label(self, text="Consultar Predio Comercial", font=("Arial", 14, "bold")).pack(pady=10)
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        self.fields = {}
        labels = [
            "ID", "Propietario", "Dirección", "Estrato",
            "Consumo m³", "Tipo Comercio", "Fecha Registro", "Código Licencia"
        ]

        for idx, label in enumerate(labels):
            tk.Label(form_frame, text=label + ":", width=18, anchor="w").grid(row=idx, column=0, padx=10, pady=3, sticky="e")
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=idx, column=1, padx=10, pady=3)
            self.fields[label] = entry
            if label != "ID":
                entry.config(state="readonly")

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="Consultar", command=self.consultar).grid(row=0, column=0, padx=10)

    def consultar(self):
        try:
            id_value = self.fields["ID"].get().strip()
            if not id_value.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero.")
                return

            url = f"http://localhost:8081/predio/buscar/{id_value}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                for label in self.fields:
                    if label != "ID":
                        self.fields[label].config(state="normal")
                        self.fields[label].delete(0, tk.END)
                self.fields["Propietario"].insert(0, data.get("propietario", ""))
                self.fields["Dirección"].insert(0, data.get("direccion", ""))
                self.fields["Estrato"].insert(0, str(data.get("estrato", "")))
                self.fields["Consumo m³"].insert(0, str(data.get("consumo", "")))
                self.fields["Tipo Comercio"].insert(0, data.get("tipoComercio", ""))
                self.fields["Fecha Registro"].insert(0, data.get("fechaRegistro", ""))
                self.fields["Código Licencia"].insert(0, data.get("numeroLicenciaComercial", ""))
                for label in self.fields:
                    if label != "ID":
                        self.fields[label].config(state="readonly")
            else:
                messagebox.showerror("Error", f"No se encontró el predio: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al consultar: {str(e)}")

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")