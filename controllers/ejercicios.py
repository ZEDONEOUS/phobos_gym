from flask import render_template, request, flash, redirect, url_for
from utilities.forms_handler import *
from services import PhobosService
from utilities.json_utilities import convert_to_json
import json

serv = PhobosService()

# Clase para el control de los ejercicios, realizacion de operaciones
# sobre las rutinas
class Ejercicios(object):
    def get_ejercicios(self):
        obj = {
            "ejercicios":serv.get("ejercicio", "")
        }
        return render_template("ejercicios.html", context = obj)


    def insertar_ejercicio(self):
        form = FormularioInsertarEjercicio(request.form)
        if request.method == 'POST':
            if form.validate():
                new_ejercicio = {
                    "Nombre": form.nombre.data,
                    "Descripcion": form.descripcion.data,
                }

                new_ejercicio_json = json.dumps(new_ejercicio)
                serv.post('ejercicio', new_ejercicio_json)

                flash("El ejercicio ha sido registrado satisfactoriamente!", "success")
                return redirect(url_for('dashboard_administrador'))
            else:
                flash("Se ha producido un herror, verifica todos los campos!", "danger")
                return render_template('insertar-ejercicio.html', form = form)

        elif request.method == 'GET':
            return render_template('insertar-ejercicio.html', form = form)


    def insertar_rutina_ejercicio(self, id):
        form = FormularioInsertarRutinaEjercicio(request.form)
        query_rutina = "query=Id:" + id
        query_e = "query=IdRutina:" + id
        rutina = serv.get("rutina", query_rutina)
        ejercicios_rutina = serv.get("rutinas_ejercicios", query_e)
        form.rutina_id.data = json.dumps(rutina[0])

        if request.method == 'POST':
            if form.validate():
                new_rutina_ejercicio = {
                    "IdRutina": form.rutina_id.data,
                    "IdEjercicio": form.new_ejercicio.data,
                }
                print colored(new_rutina_ejercicio, "yellow")
                new_rutina_ejercicio_json = convert_to_json(new_rutina_ejercicio)
                serv.post("rutinas_ejercicios", new_rutina_ejercicio_json)

                flash("Ejercicio agregado exitosamente a la rutina!", "success")
                return redirect(url_for('dashboard_administrador'))
            else:
                flash("Se ha producido un error, verifica todos los campos!", "danger")
                return render_template('insertar-rutina-ejercicio.html', form = form, rutina = rutina, ejercicios = ejercicios_rutina)

        elif request.method == "GET":
            return render_template('insertar-rutina-ejercicio.html', form = form, rutina=rutina, ejercicios = ejercicios_rutina)
