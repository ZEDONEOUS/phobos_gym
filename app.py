from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from utilities.forms_handler import *
from utilities.login_handler import LoginHandler, login_control_admin, login_control_usuario
from utilities.registro_handler import *
from controllers.components import FabricaComponentes
from services import RoguzService
from termcolor import colored
import json

app = Flask(__name__)
serv = RoguzService()
login_handler = LoginHandler()

# Enrutador pagina de inicio
@app.route('/')
def index():
    return render_template('index.html')


# Enrutador seccion de rutinas
@app.route('/rutinas')
def rutinas():
    rutinas = FabricaComponentes.crear("Rutinas")
    return rutinas.get_rutinas()


# Enrutador de rutinas por tipo de cuerpo
@app.route('/rutinas/tipo-cuerpo/<string:id>')
def rutinas_tipo_cuerpo(id):
    rutinas = FabricaComponentes.crear("Rutinas")
    return rutinas.get_rutinas_tipo_cuerpo(id)


# Enrutador detalle de rutinas
@app.route('/rutinas-detalle/<string:id>/')
def rutinas_detalle(id):
    rutinas = FabricaComponentes.crear("Rutinas")
    return rutinas.get_rutinas_detalle(id)


# Enrutador seccion de ejercicios
@app.route('/ejercicios')
def ejercicios():
    ejercicios = FabricaComponentes.crear("Ejercicios")
    return ejercicios.get_ejercicios()


# Enrutador para el registro de nuevos usuarios
@app.route('/registro-usuarios', methods = ['GET', 'POST'])
def registro_usuarios():
    registro_usuarios = RegistroUsuarios()
    return registro_usuarios.registro()


# Enrutador para el logueo de usuarios
@app.route('/login', methods=['GET', 'POST'])
def login():
    log_usr = LoginHandler()
    return log_usr.usuario()


@app.route('/login-admin', methods=['GET', 'POST'])
def login_admin():
    log_admin = LoginHandler()
    return log_admin.administrador()


# Enrutador para el dashboard de usuarios
@app.route('/dashboard-usuario')
@login_control_usuario
def dashboard_usuario():
    usuario = FabricaComponentes.crear("Usuario")
    return usuario.get_dashboard_usuario()


# Enrutador para el dashboard del administrador
@app.route('/dashboard-administrador')
@login_control_admin
def dashboard_administrador():
    admin = FabricaComponentes.crear("Administrador")
    return admin.get_dashboard()


# Enrutador para insertar rutina
@app.route('/insertar-rutina', methods=['GET', 'POST'])
@login_control_admin
def insertar_rutina():
    admin_rutinas = FabricaComponentes.crear("Rutinas")
    return admin_rutinas.insertar_rutina()


# Enrutador para eliminar rutinas
@app.route('/eliminar-rutina/<string:id>', methods=['POST'])
@login_control_admin
def eliminar_rutina(id):
    admin_rutinas = FabricaComponentes.crear("Rutinas")
    return admin_rutinas.eliminar_rutina(id)


# Enrutador agregar tipos cuerpo a rutinas
@app.route('/insertar-rutina-tipo-cuerpo/<string:id>', methods=['GET','POST'])
@login_control_admin
def insertar_rutina_tipo_cuerpo(id):
    admin_rutinas = FabricaComponentes.crear("Rutinas")
    return admin_rutinas.insertar_rutina_tipo_cuerpo(id)


# Enrutador para agregar rutinas a usuarios
@app.route('/insertar-rutina-usuario/<string:id>', methods=['GET','POST'])
@login_control_admin
def insertar_rutina_usuario(id):
    admin_rutinas = FabricaComponentes.crear("Administrador")
    return admin_rutinas.insertar_rutina_usuario(id)


# Enrutador para insertar ejercicios
@app.route('/insertar-ejercicio/', methods=['GET','POST'])
@login_control_admin
def insertar_ejercicio():
    admin_ejercicios = FabricaComponentes.crear("Ejercicios")
    return admin_ejercicios.insertar_ejercicio()


# Enrutador para agregar ejercicios a rutinas
@app.route('/insertar-rutina-ejercicio/<string:id>', methods=['GET','POST'])
@login_control_admin
def insertar_rutina_ejercicio(id):
    admin_ejercicios = FabricaComponentes.crear("Ejercicios")
    return admin_ejercicios.insertar_rutina_ejercicio(id)


# Enrutador para cerrar sesion
@app.route('/cerrar-sesion')
def cerrar_sesion():
    session.clear()
    flash('La sesion se ha cerrado satisfactoriamente', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'QWERTY12345'
    app.run(debug = True)
