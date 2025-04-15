import tkinter as tk
from tkinter import messagebox
import requests

class EliminarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eliminar")
        self.root.geometry("400x400")
        self.root.eval('tk::PlaceWindow . center')

        # Título
        tk.Label(root, text="Modulo para Eliminar", font=("Arial", 10, "bold")).grid(row=0, column=1, columnspan=2, pady=10)

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

        # Crear etiquetas y cajas de texto
        for idx, field in enumerate(self.fields.keys()):
            tk.Label(root, text=field).grid(row=idx + 1, column=0, sticky="e", padx=20, pady=2)
            entry = tk.Entry(root, width=30)
            entry.grid(row=idx + 1, column=1, padx=10, pady=2)
            self.fields[field] = entry

        # Botón Consultar
        btn_consultar = tk.Button(root, text="Consulta", command=self.consultar)
        btn_consultar.grid(row=11, column=0, pady=15)

        # Botón Eliminar
        btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar)
        btn_eliminar.grid(row=11, column=1, pady=15)

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


if __name__ == "__main__":
    root = tk.Tk()
    app = EliminarApp(root)
    root.mainloop()
