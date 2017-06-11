import requests as req
from termcolor import colored
import json


class RoguzService(object):
    # Inicializa el servicio basado en una url donde se encuentra tal
    def __init__(self):
        self.url = "http://localhost:8080/v1/"

    # Procesa una peticion get dependiendo de los parametros
    def get(self, table, params):
        result = req.get(self.url+table+'/?'+params)
        if result.status_code == req.codes.ok:
            return result.json()
        else:
            return "Imposible ejecutar operacion sobre servicio"

    # Relaiza una incescion, a traves de post dependiendo de los parametros
    def post(self, table, element):
        req.post(self.url+table, element)

    # Realiza una actuaizacion, a traves de put
    def put(self, table, id, element):
        req.put(self.url+table+'/'+id, element)

    # Borra un registri dependiendo de los parametros que le sean pasados
    def delete(self, table, id):
        req.delete(self.url+table+'/'+id)
