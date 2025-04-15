import tkinter as tk
from tkinter import messagebox
from Componentes.VentanaCrearLicencia import VentanaCrearLicencia


class GuiPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Comercial")
        self.root.geometry("600x400")

        self.crear_menu()

    def crear_menu(self):
        menu_bar = tk.Menu(self.root)

        # Menú: Predio Comercial
        predio_menu = tk.Menu(menu_bar, tearoff=0)
        predio_menu.add_command(label="Crear", command=lambda: self.mostrar_accion("Crear Predio"))
        predio_menu.add_command(label="Eliminar", command=lambda: self.mostrar_accion("Eliminar Predio"))
        predio_menu.add_command(label="Consultar", command=lambda: self.mostrar_accion("Consultar Predio"))
        predio_menu.add_command(label="Listar", command=lambda: self.mostrar_accion("Listar Predios"))
        predio_menu.add_command(label="Actualizar", command=lambda: self.mostrar_accion("Actualizar Predio"))
        menu_bar.add_cascade(label="Predio Comercial", menu=predio_menu)

        # Menú: Licencia Comercial
        licencia_menu = tk.Menu(menu_bar, tearoff=0)
        licencia_menu.add_command(label="Crear", command=self.abrir_crear_licencia)
        licencia_menu.add_command(label="Eliminar", command=lambda: self.mostrar_accion("Eliminar Licencia"))
        licencia_menu.add_command(label="Consultar", command=lambda: self.mostrar_accion("Consultar Licencia"))
        licencia_menu.add_command(label="Listar", command=lambda: self.mostrar_accion("Listar Licencias"))
        licencia_menu.add_command(label="Actualizar", command=lambda: self.mostrar_accion("Actualizar Licencia"))
        menu_bar.add_cascade(label="Licencia Comercial", menu=licencia_menu)

        # Menú: Ayuda
        ayuda_menu = tk.Menu(menu_bar, tearoff=0)
        ayuda_menu.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
        menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

        self.root.config(menu=menu_bar)

    def mostrar_accion(self, texto):
        messagebox.showinfo("Acción seleccionada", f"Has seleccionado: {texto}")

    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Hecho por:\nJuanita Rodriguez\nStiven Alvarez \nBrayhan Ortegon ")

    
    def abrir_crear_licencia(self):
        VentanaCrearLicencia(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuiPrincipal(root)
    root.mainloop()
