import tkinter as tk
from tkinter import ttk, messagebox
import requests

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

        self.tree = ttk.Treeview(frame_tabla, columns=("Numero", "Expedicion", "Vencimiento", "Estado"), show="headings")
        self.tree.heading("Numero", text="Número de Licencia")
        self.tree.heading("Expedicion", text="Fecha Expedición")
        self.tree.heading("Vencimiento", text="Fecha Vencimiento")
        self.tree.heading("Estado", text="Estado")

        self.tree.column("Numero", width=150, anchor="center")
        self.tree.column("Expedicion", width=150, anchor="center")
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
        try:
            url = "http://localhost:8081/licencia/listar"  # Reemplaza con tu endpoint real
            response = requests.get(url)
            if response.status_code == 200:
                licencias = response.json()
                filtradas = []

                for licencia in licencias:
                    estado = licencia["estado"]
                    if self.estado_var.get() and estado != self.estado_var.get():
                        continue
                    filtradas.append(licencia)

                self.mostrar_datos(filtradas)
            else:
                messagebox.showerror("Error", f"No se pudo obtener datos.\nCódigo: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectarse al servidor: {str(e)}")

    def mostrar_datos(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for licencia in data:
            self.tree.insert("", "end", values=(
                licencia["numeroLicencia"],
                licencia["fechaExpedicion"],
                licencia["fechaVencimiento"],
                licencia["estado"]
            ))

    def center_window(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"+{x}+{y}")
