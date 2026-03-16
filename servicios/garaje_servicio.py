# Servicio que maneja la lógica del garaje

from modelos.vehiculo import Vehiculo


class GarajeServicio:

    def __init__(self):
        # lista donde se guardan los vehículos
        self.vehiculos = []

    def agregar_vehiculo(self, placa, marca, propietario):

        vehiculo = Vehiculo(placa, marca, propietario)

        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self):

        return self.vehiculos
