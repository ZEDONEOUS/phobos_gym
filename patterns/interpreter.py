#!/usr/bin/python

import abc

# Declara un interprete abstracto con una operacion en comun para los nodos
class InscripcionCursos(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interpretar(self):
        pass

# Implementa una operacion para los cursos abiertos
class CursoAbierto(InscripcionCursos):
    def __init__(self, expression):
        self._expression = expression

    def interpretar(self):
        self._expression.interpretar()

# Implementa una operacion para los cursos cerrados compuesto de abiertos
class CuersoCerrado(InscripcionCursos):
    def interpretar(self):
        pass


def main():
    interprete = CursoAbierto(CuersoCerrado())
    interprete.interpretar()
