from clases.vehiculo import Vehiculo

class Moto(Vehiculo):

    def __init__(self, placa):

        super().__init__(
            placa.upper(),
            "Moto",
            "Liviano"
        )

    def calcular_tarifa(self):
        return 0