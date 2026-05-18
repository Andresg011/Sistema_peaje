class Peaje:

    def __init__(self):

        # COMPOSICIÓN: el peaje contiene vehículos
        self._vehiculos = []

    # AGREGAR VEHÍCULO
    def agregar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    # OBTENER LISTA DE VEHÍCULOS
    def obtener_vehiculos(self):
        return self._vehiculos

    # CALCULAR TOTAL RECAUDADO
    def calcular_total_recaudado(self):

        total = 0

        for vehiculo in self._vehiculos:
            total += vehiculo.calcular_tarifa()

        return total

    # CONTAR VEHÍCULOS
    def contar_vehiculos(self):

        return len(self._vehiculos)

    # LIMPIAR REGISTROS (opcional útil para pruebas)
    def limpiar(self):
        self._vehiculos = []