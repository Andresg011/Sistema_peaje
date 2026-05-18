from datetime import datetime

class Vehiculo:

    # CONSTRUCTOR
    def __init__(self, placa, tipo_vehiculo, categoria):

        # ENCAPSULAMIENTO
        self._placa = placa
        self._tipo_vehiculo = tipo_vehiculo
        self._categoria = categoria

        # FECHA Y HORA AUTOMÁTICA
        ahora = datetime.now()

        self._fecha = ahora.strftime("%d/%m/%Y")
        self._hora = ahora.strftime("%H:%M:%S")

    # GETTERS
    def obtener_placa(self):
        return self._placa

    def obtener_tipo(self):
        return self._tipo_vehiculo

    def obtener_categoria(self):
        return self._categoria

    def obtener_fecha(self):
        return self._fecha

    def obtener_hora(self):
        return self._hora

    # SETTER
    def cambiar_placa(self, nueva_placa):
        self._placa = nueva_placa

    # POLIMORFISMO
    # Este método será sobrescrito por las clases hijas
    def calcular_tarifa(self):
        return 0

    # MOSTRAR INFORMACIÓN
    def mostrar_informacion(self):

        return f"""
        Tipo: {self._tipo_vehiculo}
        Placa: {self._placa}
        Categoría: {self._categoria}
        Fecha: {self._fecha}
        Hora: {self._hora}
        Tarifa: ${self.calcular_tarifa()}
        """