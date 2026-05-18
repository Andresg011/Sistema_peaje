class Peaje:

    def __init__(self):
        self._vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self._vehiculos

    def calcular_total_recaudado(self):

        total = 0

        for vehiculo in self._vehiculos:
            total += vehiculo.calcular_tarifa()

        return total

    def contar_vehiculos(self):
        return len(self._vehiculos)

    def limpiar(self):
        self._vehiculos = []