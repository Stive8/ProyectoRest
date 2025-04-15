import tkinter as tk
from tkinter import messagebox

class VentanaActualizarLicencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Actualizar Licencia Comercial")
        self.geometry("400x420")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        titulo = tk.Label(self, text="Actualizar Licencia Comercial", font=("Arial", 16))
        titulo.pack(pady=20)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        # Campo: Número de Licencia (editable)
        tk.Label(form_frame, text="Número de Licencia:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_numero = tk.Entry(form_frame)
        self.entry_numero.grid(row=0, column=1, padx=5, pady=5)

        # Campo: Fecha Expedición (editable)
        tk.Label(form_frame, text="Fecha de Expedición:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_expedicion = tk.Entry(form_frame)
        self.entry_expedicion.grid(row=1, column=1, padx=5, pady=5)

        # Campo: Fecha Vencimiento (editable)
        tk.Label(form_frame, text="Fecha de Vencimiento:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_vencimiento = tk.Entry(form_frame)
        self.entry_vencimiento.grid(row=2, column=1, padx=5, pady=5)

        # Campo: Estado (editable)
        tk.Label(form_frame, text="Estado:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_estado = tk.Entry(form_frame)
        self.entry_estado.grid(row=3, column=1, padx=5, pady=5)

        # Botón: Consultar
        btn_consultar = tk.Button(self, text="Consultar", command=self.consultar_licencia)
        btn_consultar.pack(pady=10)

        # Botón: Actualizar
        btn_actualizar = tk.Button(self, text="Actualizar", command=self.actualizar_licencia)
        btn_actualizar.pack(pady=5)

    def consultar_licencia(self):
        numero = self.entry_numero.get()
        if numero == "12345":
            self.entry_expedicion.delete(0, tk.END)
            self.entry_expedicion.insert(0, "2024-01-01")

            self.entry_vencimiento.delete(0, tk.END)
            self.entry_vencimiento.insert(0, "2025-01-01")

            self.entry_estado.delete(0, tk.END)
            self.entry_estado.insert(0, "Activa")
        else:
            messagebox.showwarning("No encontrada", f"No se encontró licencia con número: {numero}")
            self.limpiar_campos()

    def actualizar_licencia(self):
        numero = self.entry_numero.get()
        expedicion = self.entry_expedicion.get()
        vencimiento = self.entry_vencimiento.get()
        estado = self.entry_estado.get()

        if not numero or not expedicion or not vencimiento or not estado:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        # Aquí se haría el PUT real por REST
        messagebox.showinfo("Actualizado", f"Licencia {numero} actualizada correctamente.")

    def limpiar_campos(self):
        self.entry_expedicion.delete(0, tk.END)
        self.entry_vencimiento.delete(0, tk.END)
        self.entry_estado.delete(0, tk.END)

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
