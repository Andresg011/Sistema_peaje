from datetime import datetime

class Moto:

    def __init__(self, placa):

        # IDENTIDAD DEL VEHÍCULO
        self._placa = placa
        self._tipo_vehiculo = "Moto"
        self._categoria = "Liviano"

        # FECHA Y HORA DEL REGISTRO
        self._fecha = datetime.now().strftime("%Y-%m-%d")
        self._hora = datetime.now().strftime("%H:%M:%S")

    # TARIFA (MOTOS NO PAGAN)
    def calcular_tarifa(self):
        return 0

    # REPRESENTACIÓN DEL OBJETO
    def __str__(self):
        return f"Moto {self._placa}"