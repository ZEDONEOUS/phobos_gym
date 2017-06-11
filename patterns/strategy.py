#!/usr/bin/python

import abc

# Define la interfaz de acceso para el cliente
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.interface_algoritmo()

# Declara una interface comun para todas las especificaciones
class AsignarEspacio(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_algoritmo(self):
        pass

# Implementa el algoritmo utilizando Asignar espacio
class EspacioBaile(AsignarEspacio):
    def interface_algoritmo(self):
        print "Define un nuevo espacio de baile"

# Implementa el algoritmo utilizando Asignar espacio
class EspacioRutinas(AsignarEspacio):
    def interface_algoritmo(self):
        print "Define un nuevo espacio de ejecucion de rutinas"


# Implementa el algoritmo utilizando Asignar espacio
class EspacioEntrenamiento(AsignarEspacio):
    def interface_algoritmo(self):
        print "define un nuevo espacio de entrenamiento especializado"


def main():
    concrete_strategy_a = EspacioBaile()
    context = Context(concrete_strategy_a)
    context.context_interface()
