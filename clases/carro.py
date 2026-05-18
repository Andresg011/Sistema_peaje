from clases.vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, placa):

        super().__init__(
            placa,
            "Carro",
            "Categoría 2"
        )

    # POLIMORFISMO
    def calcular_tarifa(self):
        return 12000