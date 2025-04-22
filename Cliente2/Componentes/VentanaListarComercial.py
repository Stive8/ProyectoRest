import tkinter as tk
from tkinter import ttk, messagebox
import requests

class VentanaListarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Listar Predios Comerciales")
        self.geometry("700x400")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        # Título
        tk.Label(self, text="Listar Predios Comerciales", font=("Arial", 14, "bold")).pack(pady=10)

        # Frame para la tabla
        frame_tabla = tk.Frame(self)
        frame_tabla.pack(padx=10, pady=10, fill="both", expand=True)

        # Treeview
        columnas = ("ID", "Propietario", "Estrato", "Consumo", "Tipo Comercio", "Código Licencia")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # Frame para filtros y botón
        frame_filtros = tk.Frame(self)
        frame_filtros.pack(pady=10)

        self.estrato_var = tk.StringVar(value="")
        tk.Radiobutton(frame_filtros, text="Estrato 1-3", variable=self.estrato_var, value="bajo").grid(row=0, column=0, padx=5)
        tk.Radiobutton(frame_filtros, text="Estrato 4-6", variable=self.estrato_var, value="alto").grid(row=0, column=1, padx=5)
        tk.Button(frame_filtros, text="Listar", command=self.listar).grid(row=0, column=2, padx=10)

    def listar(self):
        try:
            url = "http://localhost:8081/predio/listar"
            response = requests.get(url)
            if response.status_code == 200:
                predios = response.json()
                filtrados = []

                for predio in predios:
                    estrato = predio.get("estrato", 0)
                    if self.estrato_var.get() == "bajo" and not (1 <= estrato <= 3):
                        continue
                    elif self.estrato_var.get() == "alto" and not (4 <= estrato <= 6):
                        continue
                    filtrados.append(predio)

                self.mostrar_datos(filtrados)
            else:
                messagebox.showerror("Error", f"No se pudo obtener datos: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectarse al servidor: {str(e)}")

    def mostrar_datos(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for predio in data:
            self.tree.insert("", "end", values=(
                predio.get("id", ""),
                predio.get("propietario", ""),
                predio.get("estrato", ""),
                predio.get("consumo", ""),
                predio.get("tipoComercio", ""),
                predio.get("codigoLicencia", "")
            ))

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")