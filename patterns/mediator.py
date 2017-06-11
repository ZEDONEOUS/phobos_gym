#!/usr/bin/python

# Clase que mantiene la comunicacion entre los colegas
class Mediator:
    def __init__(self):
        self.colega_1 = Clientes(self)
        self.colega_2 = Administrador(self)
        self.colega_3 = MicroServicioDatos(self)


# Interface que define la operacion de los coegas
class Colegas(object):
    def operacion(self): pass

# Colega que conoce a su mediador y ejecuta operaciones
class Clientes(Colegas):
    def __init__(self, mediator):
        self._mediator = mediator

    def operacion(self):
        print "Comunicacion con Clientes"

# Colega que conoce a su mediador y ejecuta operaciones
class Administrador(Colegas):
    def __init__(self, mediator):
        self._mediator = mediator

    def operacion(self):
        print "Comunicacion con Administrador"

# Colega que conoce a su mediador y ejecuta operaciones
class MicroServicioDatos(Colegas):
    def __init__(self, mediator):
        self._mediator = mediator

    def operacion(self):
        print "Comunicacion con MicroServicioDatos"
