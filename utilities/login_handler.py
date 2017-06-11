from flask import request, render_template, flash, redirect, url_for, session, logging
from passlib.hash import sha256_crypt
from utilities.forms_handler import *
from services import RoguzService
from functools import wraps
from termcolor import colored

serv = RoguzService()

class LoginHandler(object):
    def usuario(self):
        form = FormularioLogueo(request.form)
        if request.method == 'POST' and form.validate():
            logueo = {
                "usuario":form.usuario.data,
                "contrasena":form.contrasena.data
            }
            usuario = serv.get("usuario", "query=Usuario:"+str(logueo['usuario']))
            if usuario:
                print colored(usuario, 'red')
                if sha256_crypt.verify(logueo['contrasena'], usuario[0]['Contrasena']):
                    session['admin'] = False
                    session['logueado'] = True
                    session['id_usuario'] = usuario[0]['Id']
                    session['nombre'] = usuario[0]['Nombre']
                    session['usuario'] = logueo['usuario']
                    return redirect(url_for('dashboard_usuario'))
            else:
                flash('El usuario ingresado no se encuentra registrado!', 'warning')

        return render_template('login.html', form = form)


    def administrador(self):
        form = FormularioLogueo(request.form)
        if request.method == 'POST' and form.validate():
            logueo = {
                "usuario":form.usuario.data,
                "contrasena":form.contrasena.data
            }
            usuario = serv.get("administrador", "query=Usuario:"+str(logueo['usuario']))
            print colored(usuario, "green")
            if usuario:
                if sha256_crypt.verify(logueo['contrasena'], usuario[0]['Contrasena']):
                    session['admin'] = True
                    session['logueado'] = True
                    session['nombre'] = usuario[0]['Nombre']
                    session['usuario'] = logueo['usuario']
                    return redirect(url_for('dashboard_administrador'))
            else:
                flash('El usuario de admin ingresado no se encuentra registrado!', 'warning')

        return render_template('login-admin.html', form = form)


# Funcion para el control de paginas restringidas admin
def login_control_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logueado' in session and session['admin']:
            return f(*args, **kwargs)
        else:
            flash("Acceso denegado!, por favor ingrese sus credenciales", 'danger')
            return redirect(url_for('login'))
    return wrap

# Funcion para el control de paginas restringidas usuarios
def login_control_usuario(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logueado' in session:
            return f(*args, **kwargs)
        else:
            flash("Acceso denegado!, por favor ingrese sus credenciales", 'danger')
            return redirect(url_for('login'))
    return wrap
