from clases.vehiculo import Vehiculo

class TractoCamion(Vehiculo):

    def __init__(self, placa, ejes):

        super().__init__(
            placa.upper(),
            "Tractocamión",
            "Categoría 4"
        )

        self._ejes = ejes

    def obtener_ejes(self):
        return self._ejes

    def calcular_tarifa(self):

        tarifa_base = 30000
        valor_por_eje = 8000

        return tarifa_base + (self._ejes * valor_por_eje)