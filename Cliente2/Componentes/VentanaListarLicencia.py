import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

class LicenciaConsulta:
    """Clase para manejar la lógica de consulta de licencias al servidor."""
    
    BASE_URL = "http://localhost:8081/licencia"

    @staticmethod
    def listar_licencias():
        """
        Obtiene la lista de licencias comerciales desde el servidor.
        Retorna la lista de licencias o None si hay un error.
        """
        try:
            url = f"{LicenciaConsulta.BASE_URL}/listar"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Error del servidor: Código {response.status_code}")

        except requests.exceptions.Timeout:
            raise Exception("Tiempo de espera agotado al conectar con el servidor")
        except requests.exceptions.ConnectionError:
            raise Exception("Error de conexión con el servidor")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error en la solicitud: {str(e)}")

class VentanaListarLicencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Listar Licencias Comerciales")
        self.geometry("700x400")
        self.resizable(False, False)
        self.center_window()

        # Frame para la tabla
        frame_tabla = tk.Frame(self)
        frame_tabla.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame_tabla, columns=("Numero", "Representante", "Vencimiento", "Estado"), show="headings")
        self.tree.heading("Numero", text="Número de Licencia")
        self.tree.heading("Representante", text="Representante Legal")
        self.tree.heading("Vencimiento", text="Fecha Vencimiento")
        self.tree.heading("Estado", text="Estado")

        self.tree.column("Numero", width=150, anchor="center")
        self.tree.column("Representante", width=200, anchor="center")
        self.tree.column("Vencimiento", width=150, anchor="center")
        self.tree.column("Estado", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # Frame para filtros
        frame_filtros = tk.Frame(self)
        frame_filtros.pack(pady=10)

        self.estado_var = tk.StringVar(value="")

        tk.Radiobutton(frame_filtros, text="Activas", variable=self.estado_var, value="Activa").grid(row=0, column=0, padx=5)
        tk.Radiobutton(frame_filtros, text="Inactivas", variable=self.estado_var, value="Inactiva").grid(row=0, column=1, padx=5)
        tk.Button(frame_filtros, text="Listar", command=self.listar).grid(row=0, column=2, padx=10)

    def listar(self):
        """Obtiene y muestra la lista de licencias según el filtro seleccionado."""
        try:
            licencias = LicenciaConsulta.listar_licencias()
            if licencias is None:
                messagebox.showerror("Error", "No se pudo obtener la lista de licencias.")
                return

            filtradas = []
            fecha_actual = datetime.now()

            for licencia in licencias:
                try:
                    fecha_vencimiento = datetime.strptime(licencia.get("fechaVencimiento", ""), "%Y-%m-%d")
                    estado = "Activa" if fecha_vencimiento >= fecha_actual else "Inactiva"
                except ValueError:
                    estado = "Desconocido"  # En caso de formato de fecha inválido

                if not self.estado_var.get() or estado == self.estado_var.get():
                    filtradas.append({
                        "codigo": licencia.get("codigo", ""),
                        "representanteLegal": licencia.get("representanteLegal", ""),
                        "fechaVencimiento": licencia.get("fechaVencimiento", ""),
                        "estado": estado
                    })

            self.mostrar_datos(filtradas)

        except Exception as e:
            messagebox.showerror("Error", f"Error al conectarse al servidor: {str(e)}")

    def mostrar_datos(self, data):
        """Muestra las licencias en la tabla."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for licencia in data:
            self.tree.insert("", "end", values=(
                licencia["codigo"],
                licencia["representanteLegal"],
                licencia["fechaVencimiento"],
                licencia["estado"]
            ))

    def center_window(self):
        """Centra la ventana en la pantalla."""
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana principal
    ventana = VentanaListarLicencia(root)
    ventana.mainloop()