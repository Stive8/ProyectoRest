import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests
import json

# Función que se llama al hacer clic en "Crear"
def crear_comercial():
    try:
        data = {
            "propietario": entry_propietario.get().strip(),
            "direccion": entry_direccion.get().strip(),
            "fechaRegistro": entry_fecha.get().strip(),
            "estadoCuenta": entry_estado.get().strip(),
            "estrato": int(entry_estrato.get().strip()),
            "consumo": float(entry_consumo.get().strip()),
            "subsidio": int(entry_subsidio.get().strip()),
            "tipoVivienda": entry_vivienda.get().strip()
        }

        response = requests.post(
            url="http://localhost:8081/predio/crear",
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        messagebox.showinfo("Resultado", f"Código de respuesta: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear ventana
ventana = tk.Tk()
ventana.title("Crear")
ventana.geometry("500x340")
ventana.resizable(False, False)

# Centrar ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')

# Etiquetas y campos de texto
tk.Label(ventana, text="Modulo para Crear", font=('Arial', 10, 'bold')).grid(row=0, column=1, pady=10)

tk.Label(ventana, text="Propietario").grid(row=1, column=0, padx=30, sticky="e")
entry_propietario = tk.Entry(ventana, width=30)
entry_propietario.grid(row=1, column=1, pady=5)

tk.Label(ventana, text="Direccion").grid(row=2, column=0, padx=30, sticky="e")
entry_direccion = tk.Entry(ventana, width=30)
entry_direccion.grid(row=2, column=1, pady=5)

tk.Label(ventana, text="Estado de Cuenta").grid(row=3, column=0, padx=30, sticky="e")
entry_estado = tk.Entry(ventana, width=30)
entry_estado.grid(row=3, column=1, padx=5)
tk.Label(ventana, text='Escribir "AC" o "INAC"').grid(row=3, column=2)

tk.Label(ventana, text="Estrato").grid(row=4, column=0, padx=30, sticky="e")
entry_estrato = tk.Entry(ventana, width=30)
entry_estrato.grid(row=4, column=1, pady=5)
tk.Label(ventana, text="Rango: 1-6").grid(row=4, column=2)

tk.Label(ventana, text="Consumo m3").grid(row=5, column=0, padx=30, sticky="e")
entry_consumo = tk.Entry(ventana, width=30)
entry_consumo.grid(row=5, column=1, pady=5)

tk.Label(ventana, text="Subsidio").grid(row=6, column=0, padx=30, sticky="e")
entry_subsidio = tk.Entry(ventana, width=30)
entry_subsidio.grid(row=6, column=1, pady=5)

tk.Label(ventana, text="Tipo Vivienda").grid(row=7, column=0, padx=30, sticky="e")
entry_vivienda = tk.Entry(ventana, width=30)
entry_vivienda.grid(row=7, column=1, pady=5)

tk.Label(ventana, text="Fecha Registro").grid(row=8, column=0, padx=30, sticky="e")
entry_fecha = tk.Entry(ventana, width=30)
entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
entry_fecha.grid(row=8, column=1, pady=5)

# Botón para crear
btn_crear = tk.Button(ventana, text="Crear", command=crear_comercial)
btn_crear.grid(row=9, column=1, pady=20)

ventana.mainloop()
