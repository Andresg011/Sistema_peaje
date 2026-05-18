from clases.vehiculo import Vehiculo

class Camion(Vehiculo):

    def __init__(self, placa, ejes):

        super().__init__(
            placa.upper(),
            "Camión",
            "Categoría 3"
        )

        self._ejes = ejes

    def obtener_ejes(self):
        return self._ejes

    def calcular_tarifa(self):

        tarifa_base = 18000
        valor_por_eje = 5000

        return tarifa_base + (self._ejes * valor_por_eje)