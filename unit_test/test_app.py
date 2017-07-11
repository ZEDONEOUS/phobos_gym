#!usr/bin/python
import sys
sys.path.append("../")
from services import PhobosService
from controllers.components import FabricaComponentes
from utilities.json_utilities import convert_to_json

serv = PhobosService()

# Funcion para el desarrollo de pruebas sobre la obtencion de rutinas
def test_carga_rutinas():
    obj = {
        "rutinas": serv.get("rutinas", "")
    }
    assert len(obj) > 0, "Error al traer los datos de las rutinas"


# Funcion para el desarrollo de pruebas sobre la carga de usuarios
def test_carga_usuario():
    query_u = "query=Usuario:diana"
    obj = {
        "usuario": serv.get("usuario", query_u)
    }
    assert len(obj) > 0, "Error al traer los datos del usuario" + str(obj)

# Funcion para el desarrollo de pruebas sobre
# la conversion de diccionarios de python a json
def test_conversion_json():
    obj = {
        "usuario": "usuario_prueba",
        "pass": "pass_prueba"
    }

    json_converted = convert_to_json(obj)
    assert json_converted != obj, "Error durante la conversion de diccionario a json"

# Funcion para el desarrollo de pruebas sobre la carga de modulos
def test_carga_modulos():
    usuario = FabricaComponentes.crear("Usuario")
    assert usuario != None, "Imposible desarrollar la carga del modulo de usuarios"

    rutina = FabricaComponentes.crear("Rutinas")
    assert rutina != None, "Imposible desarrollar la carga del modulo de rutina"

    ejercicios = FabricaComponentes.crear("Ejercicios")
    assert ejercicios != None, "Imposible desarrollar la carga del modulo de ejercicios"
