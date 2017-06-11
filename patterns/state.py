#!/usr/bin/python

import abc

# Define la interfaz para los clientes
class Contexto:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# Clase abstracta que encapsula el comportamiento de estados
class RegistroCliente(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self):
        pass

# Implementa la clase abstracta para el comportamiento de estado
class ClienteActivo(RegistroCliente):
    def handle(self):
        print "Comportamiento cliente activo"

# Implementa la clase abstracta para el segundo comportamiento
class ClienteInactivo(RegistroCliente):
    def handle(self):
        print "Comportamiento cliente inactivo"


def main():
    concrete_state_a = ClienteActivo()
    context = Contexto(concrete_state_a)
    context.request()
