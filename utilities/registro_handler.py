from flask import request, render_template, flash, url_for, redirect
from services import RoguzService
from utilities.forms_handler import *
from passlib.hash import sha256_crypt
import json

serv = RoguzService()

class RegistroUsuarios(object):
    def registro(self):
        form = FormularioRegistro(request.form)
        if request.method == 'POST':
            if form.validate():
                new_usuario = {
                    "Nombre": form.nombre.data,
                    "Apellido": form.apellido.data,
                    "Usuario": form.usuario.data,
                    "Email": form.email.data,
                    "Contrasena": sha256_crypt.encrypt(str(form.contrasena.data))
                }
                new_usuario_json = json.dumps(new_usuario)
                serv.post("usuario", new_usuario_json)
                flash('Ahora te encuentras registrado, te puedes loguear', 'success')
                return redirect(url_for('login'))

            else:
                flash('Se ha producido un error, verifica todos los campos', 'warning')
                return render_template('registro-usuarios.html', form=form)

        elif request.method == 'GET':
            return render_template('registro-usuarios.html', form=form)
