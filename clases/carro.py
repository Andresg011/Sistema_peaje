from clases.vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, placa):

        super().__init__(
            placa.upper(),
            "Carro",
            "Categoría 2"
        )

    def calcular_tarifa(self):
        return 12000