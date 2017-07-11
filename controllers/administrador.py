from flask import render_template, request, flash, redirect, url_for
from utilities.forms_handler import *
from services import PhobosService
from utilities.json_utilities import convert_to_json
import json
from datetime import date

serv = PhobosService()

# Clase para la implementacion y carga de operaciones
# de administradores del sitio
class Administrador(object):
    def get_dashboard(self):
        obj = {
            "ejercicios":serv.get("ejercicio", ""),
            "rutinas":serv.get("rutina", ""),
            "usuarios":serv.get("usuario", "")
        }
        return render_template("dashboard-admin.html", context = obj)

    def insertar_rutina_usuario(self, id):
        form = FormularioInsertarRutinaUsuario(request.form)
        query_usuario = "query=Id:" + id
        query_ru = "query=IdUsuario:" + id
        usuario = serv.get("usuario", query_usuario)
        rutinas_usuario = serv.get("rutinas_usuarios", query_ru)
        form.usuario_id.data = json.dumps(usuario[0])

        if request.method == 'POST':
            if form.validate():
                new_rutina_usuario = {
                    "IdUsuario": form.usuario_id.data,
                    "IdRutina": form.new_rutina.data,
                }
                new_rutina_usuario_json = convert_to_json(new_rutina_usuario)
                serv.post("rutinas_usuarios", new_rutina_usuario_json)

                flash("Rutina agregada exitosamente al usuario!", "success")
                return redirect(url_for('dashboard_administrador'))
            else:
                flash("Se ha producido un error, verifica todos los campos!", "danger")
                return render_template('insertar-rutina-usuario.html', form = form, usuario = usuario, rutinas = rutinas_usuario)

        elif request.method == "GET":
            return render_template('insertar-rutina-usuario.html', form = form, usuario = usuario, rutinas = rutinas_usuario)
