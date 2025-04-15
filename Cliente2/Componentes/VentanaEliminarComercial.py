import tkinter as tk
from tkinter import messagebox
import requests

class VentanaEliminarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Eliminar Predio")
        self.geometry("500x400")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        # Título
        titulo = tk.Label(self, text="Módulo para Eliminar", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        # Frame para el formulario
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        # Diccionario de campos
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

        # Botones
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)

        btn_consultar = tk.Button(btn_frame, text="Consultar", command=self.consultar)
        btn_consultar.grid(row=0, column=0, padx=10)

        btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=self.eliminar)
        btn_eliminar.grid(row=0, column=1, padx=10)

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

    def eliminar(self):
        try:
            id_value = self.fields["ID"].get().strip()
            if not id_value.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero.")
                return

            confirmar = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar el predio con ID {id_value}?")
            if not confirmar:
                return

            url = f"http://localhost:8081/predio/eliminar/{id_value}"
            response = requests.delete(url)

            if response.status_code == 204:
                messagebox.showinfo("Éxito", "Predio eliminado exitosamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", f"No se pudo eliminar.\nCódigo: {response.status_code}\n{response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar: {str(e)}")

    def limpiar_campos(self):
        for entry in self.fields.values():
            entry.delete(0, tk.END)

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")


