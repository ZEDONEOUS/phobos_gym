from flask import render_template, request, flash, redirect, url_for, session
from utilities.forms_handler import *
from services import RoguzService
from utilities.json_utilities import convert_to_json
import json

serv = RoguzService()

class Usuarios(object):
    def get_dashboard_usuario(self):
        query_u = "query=Usuario:" + session['usuario']
        query_ru = "query=IdUsuario:" + str(session['id_usuario'])
        obj = {
            "usuario": serv.get("usuario", query_u),
            "ejercicios":serv.get("ejercicio", ""),
            "rutinas":serv.get("rutinas_usuarios", query_ru)
        }
        return render_template("dashboard-usuario.html", context = obj)
