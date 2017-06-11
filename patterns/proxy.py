#!/usr/bin/python

# Interfaz que define las operaciones sobre los clientes
class ClienteRoguzGym(object):
    def get_rutinas():
        raise NotImplementedError()
    def get_parametros_cuenta():
        raise NotImplementedError()

# Clase proxy que representa el puente con las hojas
class Proxy(ClienteRoguzGym):
    def __init__(self):
        self.cliente_gym = ClienteGym()

    def get_rutinas(self):
        return self.cliente_gym.get_rutinas()

    def get_parametros_cuenta(self):
        return self.cliente_gym.get_parametros_cuenta()

# Especificacion de la Interfaz descrita
class ClienteGym(ClienteRoguzGym):
    def get_rutinas(self):
        return "Ares, Loki, Ra"

    def get_parametros_cuenta(self):
        return "Estado: activo, tipo_cuerpo: mesomorfo"
