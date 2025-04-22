import tkinter as tk
from tkinter import messagebox
import requests
import json
import re

class VentanaActualizarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Actualizar Predio Comercial")
        self.geometry("500x400")
        self.resizable(False, False)
        self.fields = {}  # Inicializar explícitamente
        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        tk.Label(self, text="Actualizar Predio Comercial", font=("Arial", 14, "bold")).pack(pady=10)
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        labels = ["ID", "Propietario", "Dirección", "Estrato", "Consumo m³", "Tipo Comercio", "Código Licencia"]
        for idx, label in enumerate(labels):
            tk.Label(form_frame, text=label + ":", width=18, anchor="w").grid(row=idx, column=0, padx=10, pady=3, sticky="e")
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=idx, column=1, padx=10, pady=3)
            self.fields[label] = entry
            if label != "ID":
                entry.config(state="disabled")

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="Consultar", command=self.consultar).grid(row=0, column=0, padx=10)
        self.btn_actualizar = tk.Button(btn_frame, text="Actualizar", command=self.actualizar, state="disabled")
        self.btn_actualizar.grid(row=0, column=1, padx=10)

    def consultar(self):
        try:
            if "ID" not in self.fields or not self.fields["ID"]:
                messagebox.showerror("Error", "El campo ID no está inicializado correctamente.")
                return
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
                self.fields["Tipo Comercio"].insert(0, data.get("tipoComercio", "") or "Sin especificar")
                self.fields["Código Licencia"].insert(0, data.get("numeroLicenciaComercial", ""))
                self.btn_actualizar.config(state="normal")
            elif response.status_code == 404:
                messagebox.showerror("Error", "No se encontró el predio.")
                self.btn_actualizar.config(state="disabled")
            else:
                messagebox.showerror("Error", f"Error al consultar: {response.text}")
                self.btn_actualizar.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al consultar: {str(e)}")

    def actualizar(self):
        try:
            if "ID" not in self.fields or not self.fields["ID"]:
                messagebox.showerror("Error", "El campo ID no está inicializado correctamente.")
                return
            id_value = self.fields["ID"].get().strip()
            if not id_value.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero.")
                return
            propietario = self.fields["Propietario"].get().strip()
            direccion = self.fields["Dirección"].get().strip()
            tipo_comercio = self.fields["Tipo Comercio"].get().strip()
            numero_licencia_comercial = self.fields["Código Licencia"].get().strip()
            if not all([propietario, direccion, tipo_comercio]):
                messagebox.showerror("Error", "Propietario, Dirección y Tipo Comercio son obligatorios.")
                return
            if not re.match(r'^[a-zA-Z0-9\s]+$', tipo_comercio):
                messagebox.showerror("Error", "Tipo Comercio solo puede contener letras, números y espacios.")
                return
            try:
                estrato = int(self.fields["Estrato"].get().strip())
                consumo = float(self.fields["Consumo m³"].get().strip())
                if not (1 <= estrato <= 6):
                    messagebox.showerror("Error", "Estrato debe estar entre 1 y 6.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Estrato debe ser entero y Consumo debe ser numérico.")
                return
            data = {
                "index": int(id_value),
                "propietario": propietario,
                "direccion": direccion,
                "estrato": estrato,
                "consumo": consumo,
                "tipoComercio": tipo_comercio,
                "numeroLicenciaComercial": numero_licencia_comercial
            }
            print("JSON enviado:", json.dumps(data, indent=2))
            response = requests.put(
                "http://localhost:8081/predio/actualizar",
                headers={"Content-Type": "application/json"},
                data=json.dumps(data)
            )
            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Predio actualizado exitosamente.")
                self.destroy()
            else:
                messagebox.showerror("Error", f"Error al actualizar: {response.text}\nJSON enviado: {json.dumps(data, indent=2)}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar: {str(e)}")

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")