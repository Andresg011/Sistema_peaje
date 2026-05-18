from flask import Flask, render_template, request
import re

from clases.moto import Moto
from clases.carro import Carro
from clases.camion import Camion
from clases.tractocamion import TractoCamion
from clases.peaje import Peaje

app = Flask(__name__)

peaje = Peaje()

#  VALIDACIÓN DE PLACAS COLOMBIA
def validar_placa(tipo, placa):

    placa = placa.strip().upper()

    if tipo == "Moto":
        return re.fullmatch(r"[A-Z]{3}[0-9]{2}[A-Z]?", placa)

    elif tipo in ["Carro", "Camion", "TractoCamion"]:
        return re.fullmatch(r"[A-Z]{3}[0-9]{3}", placa)

    return False


@app.route("/", methods=["GET", "POST"])
def inicio():

    mensaje = ""

    if request.method == "POST":

        placa = request.form.get("placa", "").strip().upper()
        tipo = request.form.get("tipo")
        ejes = request.form.get("ejes")

        vehiculo = None

        #  VALIDACIÓN GENERAL
        if not placa or not tipo:
            mensaje = "Error: Debe completar todos los campos"

        elif not validar_placa(tipo, placa):
            mensaje = "Error: Placa inválida para el tipo de vehículo"

        else:

            if tipo == "Moto":
                vehiculo = Moto(placa)

            elif tipo == "Carro":
                vehiculo = Carro(placa)

            elif tipo == "Camion":

                if not ejes or not ejes.isdigit():
                    mensaje = "Error: Camión requiere número de ejes"
                else:
                    ejes = int(ejes)

                    if ejes < 2 or ejes > 10:
                        mensaje = "Error: Número de ejes inválido"
                    else:
                        vehiculo = Camion(placa, ejes)

            elif tipo == "TractoCamion":

                if not ejes or not ejes.isdigit():
                    mensaje = "Error: Tractocamión requiere número de ejes"
                else:
                    ejes = int(ejes)

                    if ejes < 2 or ejes > 12:
                        mensaje = "Error: Número de ejes inválido"
                    else:
                        vehiculo = TractoCamion(placa, ejes)

            # REGISTRO FINAL DEL VEHÍCULO
            if vehiculo:
                peaje.agregar_vehiculo(vehiculo)
                mensaje = f"Vehículo registrado correctamente. Valor: ${vehiculo.calcular_tarifa()}"

    return render_template(
        "index.html",
        vehiculos=peaje.obtener_vehiculos(),
        total=peaje.calcular_total_recaudado(),
        total_vehiculos=peaje.contar_vehiculos(),
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)