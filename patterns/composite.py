#!/usr/bin/python

# Clase abstracta desarrollod e componente
class ServicioAbstracto(object):
    def __init__(self, *args, **kw): pass

    def component_function(self): pass

# Hojas que representan los servicios
class Servicios(ServicioAbstracto):
    def __init__(self, *args, **kw):
        ServicioAbstracto.__init__(self, *args, **kw)

    def component_function(self):
        print "Servicio de clases de baile"

# clase compuesta de servicios
class Promociones(ServicioAbstracto):
    def __init__(self, *args, **kw):
        ServicioAbstracto.__init__(self, *args, **kw)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        map(lambda x: x.component_function(), self.children)
