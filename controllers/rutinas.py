from flask import render_template, request, flash, redirect, url_for
from utilities.forms_handler import *
from services import RoguzService
from utilities.json_utilities import convert_to_json
import json

serv = RoguzService()
class Rutinas(object):
    def get_rutinas(self):
        obj = {
            "rutinas": serv.get("rutina", ""),
            "tipos_cuerpo": serv.get("tipo_cuerpo", "")
        }
        return render_template('rutinas.html', context = obj)

    def get_rutinas_detalle(self, id):
        query = 'query=IdRutina:' + id
        obj = {
            "rutina":serv.get("rutina", "query=Id:" + id),
            "tipo_cuerpo":serv.get("rutinas_tipos_cuerpo", query),
            "ejercicios":serv.get("rutinas_ejercicios", query)
        }
        return render_template('rutinas_detalle.html', context = obj)

    def get_rutinas_tipo_cuerpo(self, id):
        query = 'query=IdTipoCuerpo:' + id
        obj = {
            "titulo":serv.get('tipo_cuerpo', "query=Id:" + id),
            "rutinas":serv.get('rutinas_tipos_cuerpo', query),
            "tipos_cuerpo": serv.get("tipo_cuerpo", "")
        }
        return render_template('rutinas_tipo_cuerpo.html', context = obj)


    def insertar_rutina(self):
        form = FormularioInsertarRutina(request.form)
        if request.method == 'POST':
            if form.validate():
                new_rutina = {
                    "Nombre": form.nombre.data,
                    "Descripcion": form.descripcion.data
                }
                new_rutina_json = json.dumps(new_rutina)
                serv.post('rutina', new_rutina_json)

                flash("la rutina ha sido registrada satisfactoriamente!", "success")
                return redirect(url_for('dashboard_administrador'))
            else:
                flash("Se ha producido un herror, verifica todos los campos!", "danger")
                return render_template('insertar-rutina.html', form = form)

        elif request.method == 'GET':
            return render_template('insertar-rutina.html', form = form)

    def eliminar_rutina(self, id):
        query_rtc = "query=IdRutina:" + id
        rutina_tipos_cuerpo = serv.get("rutinas_tipos_cuerpo", query_rtc)
        rutina_ejercicios = serv.get("rutinas_ejercicios", query_rtc)

        if rutina_tipos_cuerpo:
            for idr in rutina_tipos_cuerpo:
                serv.delete("rutinas_tipos_cuerpo", str(idr["Id"]))

        if rutina_ejercicios:
            for idr in rutina_ejercicios:
                serv.delete("rutinas_ejercicios", str(idr["Id"]))

        serv.delete("rutina", id)

        flash("Rutina Eliminada exitosamente!", "success")
        return redirect(url_for('dashboard_administrador'))


    def insertar_rutina_tipo_cuerpo(self, id):
        form = FormularioInsertarRutinaTipoCuerpo(request.form)
        query_rutina = "query=Id:" + id
        query_tc = "query=IdRutina:" + id
        rutina = serv.get("rutina", query_rutina)
        tipos_cuerpo_rutina = serv.get("rutinas_tipos_cuerpo", query_tc)
        form.rutina_id.data = json.dumps(rutina[0])

        if request.method == 'POST':
            if form.validate():
                new_rutina_tipo_cuerpo = {
                    "IdRutina": form.rutina_id.data,
                    "IdTipoCuerpo": form.new_tipo_cuerpo.data,
                }
                new_rutina_tipo_cuerpo_json = convert_to_json(new_rutina_tipo_cuerpo)
                serv.post("rutinas_tipos_cuerpo", new_rutina_tipo_cuerpo_json)

                flash("Tipo cuerpo agregado exitosamente a la rutina!", "success")
                return redirect(url_for('dashboard_administrador'))
            else:
                flash("Se ha producido un error, verifica todos los campos!", "danger")
                return render_template('insertar-rutina-tipo-cuerpo.html', form = form, rutina = rutina, tipos_cuerpo = tipos_cuerpo_rutina)

        elif request.method == "GET":
            return render_template('insertar-rutina-tipo-cuerpo.html', form = form, rutina=rutina, tipos_cuerpo = tipos_cuerpo_rutina)
