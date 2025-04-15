import tkinter as tk
from tkinter import messagebox

class VentanaEliminarLicencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Eliminar Licencia Comercial")
        self.geometry("400x420")
        self.resizable(False, False)

        self.crear_componentes()
        self.centrar_ventana()

    def crear_componentes(self):
        titulo = tk.Label(self, text="Eliminar Licencia Comercial", font=("Arial", 16))
        titulo.pack(pady=20)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        # Campo: Número de Licencia (editable)
        tk.Label(form_frame, text="Número de Licencia:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_numero = tk.Entry(form_frame)
        self.entry_numero.grid(row=0, column=1, padx=5, pady=5)

        # Campo: Fecha Expedición (no editable)
        tk.Label(form_frame, text="Fecha de Expedición:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_expedicion = tk.Entry(form_frame, state="readonly")
        self.entry_expedicion.grid(row=1, column=1, padx=5, pady=5)

        # Campo: Fecha Vencimiento (no editable)
        tk.Label(form_frame, text="Fecha de Vencimiento:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_vencimiento = tk.Entry(form_frame, state="readonly")
        self.entry_vencimiento.grid(row=2, column=1, padx=5, pady=5)

        # Campo: Estado (no editable)
        tk.Label(form_frame, text="Estado:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_estado = tk.Entry(form_frame, state="readonly")
        self.entry_estado.grid(row=3, column=1, padx=5, pady=5)

        # Botón de consultar
        btn_consultar = tk.Button(self, text="Consultar", command=self.consultar_licencia)
        btn_consultar.pack(pady=10)

        # Botón de eliminar
        btn_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_licencia)
        btn_eliminar.pack(pady=5)

    def consultar_licencia(self):
        numero = self.entry_numero.get()
        
        # Simulación de búsqueda (esto se reemplazará luego con consulta REST)
        if numero == "12345":
            self.set_readonly_fields("2024-01-01", "2025-01-01", "Activa")
        else:
            messagebox.showwarning("No encontrada", f"No se encontró licencia con número: {numero}")
            self.set_readonly_fields("", "", "")

    def eliminar_licencia(self):
        numero = self.entry_numero.get()
        if not numero:
            messagebox.showwarning("Advertencia", "Primero debes consultar una licencia.")
            return
        
        confirm = messagebox.askyesno("Confirmar", f"¿Deseas eliminar la licencia {numero}?")
        if confirm:
            # Aquí se haría el DELETE real por REST
            messagebox.showinfo("Eliminada", f"Licencia {numero} eliminada correctamente.")
            self.set_readonly_fields("", "", "")
            self.entry_numero.delete(0, tk.END)

    def set_readonly_fields(self, expedicion, vencimiento, estado):
        self.entry_expedicion.config(state="normal")
        self.entry_vencimiento.config(state="normal")
        self.entry_estado.config(state="normal")

        self.entry_expedicion.delete(0, tk.END)
        self.entry_expedicion.insert(0, expedicion)

        self.entry_vencimiento.delete(0, tk.END)
        self.entry_vencimiento.insert(0, vencimiento)

        self.entry_estado.delete(0, tk.END)
        self.entry_estado.insert(0, estado)

        self.entry_expedicion.config(state="readonly")
        self.entry_vencimiento.config(state="readonly")
        self.entry_estado.config(state="readonly")

    def centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.winfo_screenheight() // 2) - (alto // 2)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
