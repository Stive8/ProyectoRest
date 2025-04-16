import tkinter as tk
from tkinter import messagebox
import requests

class VentanaActualizarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Actualizar Predio")
        self.geometry("500x400")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        titulo = tk.Label(self, text="Módulo para Actualizar", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        self.fields = {}
        labels = [
            "ID", "Propietario", "Direccion", "Estado de Cuenta",
            "Estrato", "Consumo m3", "Subsidio", "Tipo Vivienda", "Fecha Registro"
        ]

        for idx, label in enumerate(labels):
            tk.Label(form_frame, text=label + ":", width=18, anchor="w").grid(row=idx, column=0, padx=10, pady=3, sticky="e")

            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=idx, column=1, padx=10, pady=3)
            self.fields[label] = entry

        # Deshabilitar Fecha Registro
        self.fields["Fecha Registro"].config(state="readonly")

        # Botones
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)

        btn_consultar = tk.Button(btn_frame, text="Consultar", command=self.consultar)
        btn_consultar.grid(row=0, column=0, padx=10)

        btn_actualizar = tk.Button(btn_frame, text="Actualizar", command=self.actualizar)
        btn_actualizar.grid(row=0, column=1, padx=10)

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
                self.fields["Propietario"].delete(0, tk.END)
                self.fields["Propietario"].insert(0, data["propietario"])

                self.fields["Direccion"].delete(0, tk.END)
                self.fields["Direccion"].insert(0, data["direccion"])

                self.fields["Fecha Registro"].config(state="normal")
                self.fields["Fecha Registro"].delete(0, tk.END)
                self.fields["Fecha Registro"].insert(0, data["fechaRegistro"])
                self.fields["Fecha Registro"].config(state="readonly")

                self.fields["Estado de Cuenta"].delete(0, tk.END)
                self.fields["Estado de Cuenta"].insert(0, data["estadoCuenta"])

                self.fields["Estrato"].delete(0, tk.END)
                self.fields["Estrato"].insert(0, str(data["estrato"]))

                self.fields["Consumo m3"].delete(0, tk.END)
                self.fields["Consumo m3"].insert(0, str(data["consumo"]))

                self.fields["Subsidio"].delete(0, tk.END)
                self.fields["Subsidio"].insert(0, str(data["subsidio"]))

                self.fields["Tipo Vivienda"].delete(0, tk.END)
                self.fields["Tipo Vivienda"].insert(0, data["tipoVivienda"])
            else:
                messagebox.showerror("Error", f"No se encontró el predio.\nCódigo: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al consultar: {str(e)}")

    def actualizar(self):
        try:
            id_value = self.fields["ID"].get().strip()
            if not id_value.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero.")
                return

            propietario = self.fields["Propietario"].get().strip()
            direccion = self.fields["Direccion"].get().strip()
            estado = self.fields["Estado de Cuenta"].get().strip()
            tipo_vivienda = self.fields["Tipo Vivienda"].get().strip()

            if not propietario or not direccion or not estado or not tipo_vivienda:
                messagebox.showerror("Error", "Propietario, Dirección, Estado y Tipo Vivienda no pueden estar vacíos.")
                return

            try:
                estrato = int(self.fields["Estrato"].get().strip())
                consumo = float(self.fields["Consumo m3"].get().strip())
                subsidio = float(self.fields["Subsidio"].get().strip())
            except ValueError:
                messagebox.showerror("Error", "Estrato debe ser entero y Consumo/Subsidio deben ser numéricos.")
                return

            data = {
                "id": int(id_value),
                "propietario": propietario,
                "direccion": direccion,
                "estadoCuenta": estado,
                "estrato": estrato,
                "consumo": consumo,
                "subsidio": subsidio,
                "tipoVivienda": tipo_vivienda
            }

            url = f"http://localhost:8081/predio/actualizar/{id_value}"
            response = requests.put(url, json=data)

            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Predio actualizado exitosamente.")
            else:
                messagebox.showerror("Error", f"Error al actualizar.\nCódigo: {response.status_code}\n{response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar: {str(e)}")

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
