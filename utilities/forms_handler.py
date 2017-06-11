from wtforms import Form, StringField, TextAreaField, PasswordField, SelectField, BooleanField, validators, HiddenField
from services import RoguzService
from termcolor import colored
import json

serv = RoguzService()

# Define un formulario de registro para usuarios nuevos
class FormularioRegistro(Form):
    nombre = StringField('Nombre', [validators.Length(min = 1, max = 50)])
    apellido = StringField('Apellido', [validators.Length(min = 1, max = 50)])
    usuario = StringField('Usuario', [validators.Length(min = 4, max = 25)])
    email = StringField('Email', [validators.Length(min = 4, max = 50)])
    contrasena = PasswordField('Contrasena', [
        validators.DataRequired(),
        validators.EqualTo('confirmar', message = 'Las contrasenas no coinciden')
    ])
    confirmar = PasswordField('Confirmar Contrasena')

class FormularioLogueo(Form):
    usuario = StringField('Usuario', [validators.Length(min = 1, max = 50)])
    contrasena = PasswordField('Contrasena', [
        validators.Length(min = 1, max = 50),
        validators.DataRequired()
    ])

class FormularioInsertarRutina(Form):
    nombre = StringField('Nombre', [validators.Length(min = 1, max = 50)])
    descripcion = TextAreaField('Descripcion', [validators.Length(min = 1, max = 500)])


class FormularioInsertarRutinaTipoCuerpo(Form):
    obj_tipos_cuerpos = serv.get("tipo_cuerpo", "")

    rutina_id = HiddenField("RutinaId", [validators.DataRequired()])
    rutina_nombre = StringField('Rutina', [validators.Length(min = 1, max = 50)])
    new_tipo_cuerpo = SelectField(
        'Nuevo tipo cuerpo',
        [validators.DataRequired()],
        choices = [(json.dumps(tc), tc['Descripcion']) for tc in obj_tipos_cuerpos]
    )


class FormularioInsertarEjercicio(Form):
    nombre = StringField('Nombre', [validators.Length(min = 1, max = 50)])
    descripcion = TextAreaField('descripcion', [validators.Length(min = 1, max = 500)])


class FormularioInsertarRutinaEjercicio(Form):
    obj_ejercicios = serv.get("ejercicio", "")

    rutina_id = HiddenField("RutinaId", [validators.DataRequired()])
    rutina_nombre = StringField('Rutina', [validators.Length(min = 1, max = 50)])
    new_ejercicio = SelectField(
        'Nuevo tipo cuerpo',
        [validators.DataRequired()],
        choices = [(json.dumps(ej), ej['Nombre']) for ej in obj_ejercicios]
    )


class FormularioInsertarRutinaUsuario(Form):
    obj_rutinas = serv.get("rutina", "")

    usuario_id = HiddenField("UsuarioId", [validators.DataRequired()])
    usuario_nombre = StringField('Nombre usuario', [validators.Length(min = 1, max = 50)])
    new_rutina = SelectField(
        'Nueva Rutina',
        [validators.DataRequired()],
        choices = [(json.dumps(tc), tc['Nombre']) for tc in obj_rutinas]
    )
