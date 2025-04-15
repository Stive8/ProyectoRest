import tkinter as tk
from tkinter import messagebox
import requests

class VentanaConsultarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Consultar")
        self.geometry("400x400")
        self.resizable(False, False)
        self.center_window()

        # Diccionario de campos
        self.fields = {
            "ID": None,
            "Propietario": None,
            "Direccion": None,
            "Estado de Cuenta": None,
            "Estrato": None,
            "Consumo m3": None,
            "Subsidio": None,
            "Tipo Vivienda": None,
            "Fecha Registro": None
        }

        # Título
        tk.Label(self, text="Modulo para Crear", font=("Arial", 10, "bold")).grid(row=0, column=1, columnspan=2, pady=10)

        # Crear etiquetas y cajas de texto
        for idx, field in enumerate(self.fields.keys()):
            tk.Label(self, text=field, anchor="e", width=15).grid(row=idx + 1, column=0, sticky="w", padx=10, pady=2)
            entry = tk.Entry(self, width=30)
            entry.grid(row=idx + 1, column=1, padx=10, pady=2)
            self.fields[field] = entry

        # Botón Consultar
        btn_consultar = tk.Button(self, text="Consulta", command=self.consultar)
        btn_consultar.grid(row=len(self.fields) + 1, column=1, pady=15)

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

                self.fields["Fecha Registro"].delete(0, tk.END)
                self.fields["Fecha Registro"].insert(0, data["fechaRegistro"])

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

    def center_window(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        self.geometry(f"+{x}+{y}")
