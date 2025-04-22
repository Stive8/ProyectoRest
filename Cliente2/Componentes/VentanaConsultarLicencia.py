import tkinter as tk
from tkinter import messagebox
import requests
import json

class LicenciaConsulta:
    """Clase para manejar la lógica de consulta de licencias al servidor."""
    
    BASE_URL = "http://localhost:8081/licencia"

    @staticmethod
    def consultar_licencia_por_codigo(codigo):
        """
        Consulta una licencia comercial por su código.
        Retorna la licencia si se encuentra, o None si no existe o hay un error.
        """
        try:
            url = f"{LicenciaConsulta.BASE_URL}/buscar/{codigo}"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return None
            else:
                raise Exception(f"Error del servidor: Código {response.status_code}")

        except requests.exceptions.Timeout:
            raise Exception("Tiempo de espera agotado al conectar con el servidor")
        except requests.exceptions.ConnectionError:
            raise Exception("Error de conexión con el servidor")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error en la solicitud: {str(e)}")

class VentanaConsultarLicencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Consultar Licencia Comercial")
        self.geometry("400x300")
        self.resizable(False, False)

        # Etiquetas y campos
        tk.Label(self, text="Número de Licencia:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_numero = tk.Entry(self)
        self.entry_numero.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Representante Legal:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_representante = tk.Entry(self, state="disabled")
        self.entry_representante.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Fecha de Vencimiento:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_fecha_vencimiento = tk.Entry(self, state="disabled")
        self.entry_fecha_vencimiento.grid(row=3, column=1, padx=10, pady=10)

        # Botón de consultar
        self.btn_consultar = tk.Button(self, text="Consultar", command=self.consultar_licencia)
        self.btn_consultar.grid(row=4, column=0, columnspan=2, pady=20)

    def consultar_licencia(self):
        """Maneja la consulta de una licencia al servidor."""
        codigo = self.entry_numero.get().strip()

        if not codigo:
            messagebox.showwarning("Campo vacío", "Por favor ingrese el número de licencia.")
            return

        try:
            licencia = LicenciaConsulta.consultar_licencia_por_codigo(codigo)

            if licencia:
                # Habilitar campos para edición
                self.entry_representante.config(state="normal")
                self.entry_fecha_vencimiento.config(state="normal")

                # Limpiar campos
                self.entry_representante.delete(0, tk.END)
                self.entry_fecha_vencimiento.delete(0, tk.END)

                # Insertar datos (usar get() para manejar posibles claves faltantes)
                self.entry_representante.insert(0, licencia.get("representanteLegal", ""))
                self.entry_fecha_vencimiento.insert(0, licencia.get("fechaVencimiento", ""))

                # Deshabilitar campos nuevamente
                self.entry_representante.config(state="disabled")
                self.entry_fecha_vencimiento.config(state="disabled")
            else:
                messagebox.showinfo("No encontrado", f"No se encontró una licencia con el código {codigo}.")
                # Limpiar campos en caso de no encontrar la licencia
                self.entry_representante.config(state="normal")
                self.entry_fecha_vencimiento.config(state="normal")
                self.entry_representante.delete(0, tk.END)
                self.entry_fecha_vencimiento.delete(0, tk.END)
                self.entry_representante.config(state="disabled")
                self.entry_fecha_vencimiento.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana principal
    ventana = VentanaConsultarLicencia(root)
    ventana.mainloop()