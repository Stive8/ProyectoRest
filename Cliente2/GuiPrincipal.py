import tkinter as tk
from tkinter import messagebox

class GuiPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Proyecto GUI")
        self.root.geometry("400x300")

        # Ejemplo: etiqueta
        self.label = tk.Label(root, text="¡Hola, Mundo!", font=("Arial", 14))
        self.label.pack(pady=10)

        # Ejemplo: entrada de texto
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Ejemplo: botón
        self.boton = tk.Button(root, text="Saludar", command=self.saludar)
        self.boton.pack(pady=10)

    def saludar(self):
        nombre = self.entry.get()
        messagebox.showinfo("Saludo", f"Hola, {nombre}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuiPrincipal(root)
    root.mainloop()
