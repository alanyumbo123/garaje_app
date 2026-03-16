import tkinter as tk
from tkinter import messagebox
from servicios.garaje_servicio import GarajeServicio


class GarajeApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # Campo placa
        tk.Label(root, text="Placa").grid(row=0, column=0)
        self.placa_entry = tk.Entry(root)
        self.placa_entry.grid(row=0, column=1)

        # Campo marca
        tk.Label(root, text="Marca").grid(row=1, column=0)
        self.marca_entry = tk.Entry(root)
        self.marca_entry.grid(row=1, column=1)

        # Campo propietario
        tk.Label(root, text="Propietario").grid(row=2, column=0)
        self.propietario_entry = tk.Entry(root)
        self.propietario_entry.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo).grid(row=3, column=0)
        tk.Button(root, text="Limpiar", command=self.limpiar_campos).grid(row=3, column=1)

        # Lista de vehículos
        self.lista = tk.Listbox(root, width=50)
        self.lista.grid(row=4, column=0, columnspan=2)

    def agregar_vehiculo(self):

        placa = self.placa_entry.get()
        marca = self.marca_entry.get()
        propietario = self.propietario_entry.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning("Error", "Complete todos los campos")
            return

        self.servicio.agregar_vehiculo(placa, marca, propietario)

        self.actualizar_lista()
        self.limpiar_campos()

    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for vehiculo in self.servicio.listar_vehiculos():
            self.lista.insert(tk.END, vehiculo.obtener_datos())

    def limpiar_campos(self):

        self.placa_entry.delete(0, tk.END)
        self.marca_entry.delete(0, tk.END)
        self.propietario_entry.delete(0, tk.END)
