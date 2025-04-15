import tkinter as tk
from tkinter import ttk, messagebox
import requests

class VentanaListarComercial(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Listar Predios Comerciales")
        self.geometry("700x400")
        self.resizable(False, False)
        self.center_window()

        # Frame para la tabla
        frame_tabla = tk.Frame(self)
        frame_tabla.pack(padx=10, pady=10, fill="both", expand=True)

        # Treeview (grilla)
        self.tree = ttk.Treeview(frame_tabla, columns=("ID", "Propietario", "Estado", "Estrato", "Consumo", "Subsidio"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Propietario", text="Propietario")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Estrato", text="Estrato")
        self.tree.heading("Consumo", text="Consumo m³")
        self.tree.heading("Subsidio", text="Subsidio")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Propietario", width=150, anchor="w")
        self.tree.column("Estado", width=80, anchor="center")
        self.tree.column("Estrato", width=80, anchor="center")
        self.tree.column("Consumo", width=100, anchor="center")
        self.tree.column("Subsidio", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # Frame para filtros y botón
        frame_filtros = tk.Frame(self)
        frame_filtros.pack(pady=10)

        self.estado_var = tk.StringVar(value="")
        self.estrato_var = tk.StringVar(value="")

        tk.Radiobutton(frame_filtros, text="Activar", variable=self.estado_var, value="AC").grid(row=0, column=0, padx=5)
        tk.Radiobutton(frame_filtros, text="Inactivos", variable=self.estado_var, value="INAC").grid(row=0, column=1, padx=5)

        tk.Radiobutton(frame_filtros, text="Estrato 1,2,3", variable=self.estrato_var, value="bajo").grid(row=0, column=2, padx=5)
        tk.Radiobutton(frame_filtros, text="Estrato 4,5,6", variable=self.estrato_var, value="alto").grid(row=0, column=3, padx=5)

        tk.Button(frame_filtros, text="Listar", command=self.listar).grid(row=0, column=4, padx=10)

    def listar(self):
        try:
            url = "http://localhost:8081/predio/listar"
            response = requests.get(url)
            if response.status_code == 200:
                predios = response.json()
                filtrados = []

                for predio in predios:
                    estado = predio["estadoCuenta"].upper()
                    estrato = predio["estrato"]

                    if self.estado_var.get() and estado != self.estado_var.get():
                        continue

                    if self.estrato_var.get() == "bajo" and not (1 <= estrato <= 3):
                        continue
                    elif self.estrato_var.get() == "alto" and not (4 <= estrato <= 6):
                        continue

                    filtrados.append(predio)

                self.mostrar_datos(filtrados)
            else:
                messagebox.showerror("Error", f"No se pudo obtener datos.\nCódigo: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectarse al servidor: {str(e)}")

    def mostrar_datos(self, data):
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos
        for predio in data:
            self.tree.insert("", "end", values=(
                predio["id"],
                predio["propietario"],
                predio["estadoCuenta"],
                predio["estrato"],
                predio["consumo"],
                predio["subsidio"]
            ))

    def center_window(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        self.geometry(f"+{x}+{y}")
