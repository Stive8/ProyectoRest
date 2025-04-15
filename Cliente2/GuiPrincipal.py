import tkinter as tk
from tkinter import messagebox

from Componentes.VentanaCrearComercial import VentanaCrearComercial
from Componentes.VentanaEliminarComercial import VentanaEliminarComercial
from Componentes.VentanaConsultarComercial import VentanaConsultarComercial
from Componentes.VentanaListarComercial import VentanaListarComercial
from Componentes.VentanaCrearLicencia import VentanaCrearLicencia
from Componentes.VentanaConsultarLicencia import VentanaConsultarLicencia
from Componentes.VentanaEliminarLicencia import VentanaEliminarLicencia
from Componentes.VentanaActualizarLicencia import VentanaActualizarLicencia
from Componentes.VentanaListarLicencia import VentanaListarLicencia




class GuiPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Comercial")
        self.root.geometry("600x400")

        self.crear_menu()
        self.centrar_ventana()

    def crear_menu(self):
        menu_bar = tk.Menu(self.root)

        # Menú: Predio Comercial
        predio_menu = tk.Menu(menu_bar, tearoff=0)
        predio_menu.add_command(label="Crear", command=self.abrir_crear_comercial)
        predio_menu.add_command(label="Eliminar", command=self.abrir_eliminar_comercial)
        predio_menu.add_command(label="Consultar", command=self.abrir_consultar_comercial)
        predio_menu.add_command(label="Listar", command=self.abrir_listar_comercial)
        predio_menu.add_command(label="Actualizar", command=lambda: self.mostrar_accion("Actualizar Predio"))
        menu_bar.add_cascade(label="Predio Comercial", menu=predio_menu)

        # Menú: Licencia Comercial
        licencia_menu = tk.Menu(menu_bar, tearoff=0)
        licencia_menu.add_command(label="Crear", command=self.abrir_crear_licencia)
        licencia_menu.add_command(label="Eliminar", command=self.abrir_eliminar_licencia)
        licencia_menu.add_command(label="Consultar", command=self.abrir_consultar_licencia)
        licencia_menu.add_command(label="Listar", command=self.abrir_listar_licencia)
        licencia_menu.add_command(label="Actualizar", command=self.abrir_actualizar_licencia)
        menu_bar.add_cascade(label="Licencia Comercial", menu=licencia_menu)

        # Menú: Ayuda
        ayuda_menu = tk.Menu(menu_bar, tearoff=0)
        ayuda_menu.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
        menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

        self.root.config(menu=menu_bar)

    def mostrar_accion(self, texto):
        messagebox.showinfo("Acción seleccionada", f"Has seleccionado: {texto}")

    def abrir_crear_comercial(self):
        VentanaCrearComercial(self.root)

    def abrir_consultar_comercial(self):
        VentanaConsultarComercial(self.root)


    def abrir_eliminar_comercial(self):
        VentanaEliminarComercial(self.root)

    def abrir_eliminar_licencia(self):
        VentanaEliminarLicencia(self.root)

    def abrir_crear_licencia(self):
        VentanaCrearLicencia(self.root)

    def abrir_consultar_licencia(self):
        VentanaConsultarLicencia(self.root)

    def abrir_actualizar_licencia(self):
        VentanaActualizarLicencia(self.root)

    def abrir_listar_comercial(self):
        VentanaListarComercial(self.root)

    def abrir_listar_licencia(self):
        VentanaListarLicencia(self.root)


    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Sistema Comercial v1.0\nDesarrollado en Python con Tkinter")

    def centrar_ventana(self):
        self.root.update_idletasks()

        ancho = self.root.winfo_width()
        alto = self.root.winfo_height()
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)

        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GuiPrincipal(root)
    root.mainloop()

def abrir_crear_licencia(self):
    VentanaCrearLicencia(self.root)