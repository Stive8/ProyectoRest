import tkinter as tk
from tkinter import messagebox
import requests

class VentanaEliminarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Eliminar Predio Comercial")
        self.geometry("500x400")
        self.resizable(False, False)
        self.fields = {}  # Inicializar explícitamente
        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        tk.Label(self, text="Eliminar Predio Comercial", font=("Arial", 14, "bold")).pack(pady=10)
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        labels = ["ID", "Propietario", "Dirección", "Estrato", "Consumo m³", "Tipo Comercio", "Fecha Registro", "Código Licencia"]
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
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar).grid(row=0, column=1, padx=10)

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
                self.fields["Tipo Comercio"].insert(0, data.get("tipoComercio", ""))
                self.fields["Fecha Registro"].insert(0, data.get("fechaRegistro", ""))
                self.fields["Código Licencia"].insert(0, data.get("numeroLicenciaComercial", ""))
                for label in self.fields:
                    if label != "ID":
                        self.fields[label].config(state="readonly")
            elif response.status_code == 404:
                messagebox.showerror("Error", "No se encontró el predio.")
            else:
                messagebox.showerror("Error", f"Error al consultar: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al consultar: {str(e)}")

    def eliminar(self):
        try:
            if "ID" not in self.fields or not self.fields["ID"]:
                messagebox.showerror("Error", "El campo ID no está inicializado correctamente.")
                return
            id_value = self.fields["ID"].get().strip()
            if not id_value.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero.")
                return
            confirmar = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar el predio con ID {id_value}?")
            if not confirmar:
                return
            url = f"http://localhost:8081/predio/eliminar/{id_value}"
            response = requests.delete(url)
            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Predio eliminado exitosamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", f"No se pudo eliminar: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar: {str(e)}")

    def limpiar_campos(self):
        for entry in self.fields.values():
            entry.config(state="normal")
            entry.delete(0, tk.END)
        for label in self.fields:
            if label != "ID":
                self.fields[label].config(state="readonly")

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")