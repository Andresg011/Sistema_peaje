from flask import Flask, render_template, request
import re

from clases.moto import Moto
from clases.carro import Carro
from clases.camion import Camion
from clases.tractocamion import TractoCamion
from clases.peaje import Peaje

app = Flask(__name__)

peaje = Peaje()


# VALIDACIÓN SEGURA
def validar_placa(tipo, placa):

    placa = placa.strip().upper()  # evita espacios y errores

    if tipo == "Moto":
        return re.fullmatch(r"[A-Z]{3}[0-9]{2}", placa)

    elif tipo in ["Carro", "Camion", "TractoCamion"]:
        return re.fullmatch(r"[A-Z]{3}[0-9]{3}", placa)

    return False


@app.route("/", methods=["GET", "POST"])
def inicio():

    mensaje = ""

    if request.method == "POST":

        placa = request.form["placa"]
        tipo = request.form["tipo"]
        ejes = request.form.get("ejes")

        placa = placa.strip().upper()

        vehiculo = None

        # VALIDAR PLACA
        if not validar_placa(tipo, placa):
            mensaje = "❌ Placa inválida para el tipo de vehículo"

        else:

            if tipo == "Moto":
                vehiculo = Moto(placa)

            elif tipo == "Carro":
                vehiculo = Carro(placa)

            elif tipo == "Camion":

                if not ejes or not ejes.isdigit():
                    mensaje = "❌ Camión requiere cantidad de ejes"
                else:
                    vehiculo = Camion(placa, int(ejes))

            elif tipo == "TractoCamion":

                if not ejes or not ejes.isdigit():
                    mensaje = "❌ Tractocamión requiere cantidad de ejes"
                else:
                    vehiculo = TractoCamion(placa, int(ejes))

            if vehiculo:
                peaje.agregar_vehiculo(vehiculo)
                mensaje = "✔ Vehículo registrado correctamente"

    return render_template(
        "index.html",
        vehiculos=peaje.obtener_vehiculos(),
        total=peaje.calcular_total_recaudado(),
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run(debug=True)